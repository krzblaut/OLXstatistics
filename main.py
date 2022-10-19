from db_con import DbConnect
from scrap import ScrapData
from datetime import date
import time
import logging
from progress.bar import Bar
import sys


logger = logging.getLogger(__name__)
logging.FileHandler('logfile.log')
logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')

scrap = ScrapData()
con = DbConnect('{ODBC Driver 17 for SQL Server}', 'DESKTOP-07IDHB4\SQLEXPRESS', 'OLX')
con.get_connection()


# This query gets ids of cities and districts that haven't been checked yet today plus the last city
# that has been checked today, because it could have been checked not completely.
# It returns list of tuples [(city1_id, district1_id), (city2_id, None), ...]
# None value means the city has no districts.

date = str(date.today())
ids = con.get_data(f'''
SELECT c.city_id, d.district_id
FROM (SELECT c.city_id
      FROM cities c
      LEFT JOIN (SELECT DISTINCT city_id FROM apt_prices WHERE date = '{date}' 
                    ORDER BY city_id DESC OFFSET 1 ROWS FETCH NEXT 250 ROWS ONLY) o
      ON c.city_id = o.city_id
      WHERE o.city_id IS NULL) c
LEFT JOIN districts d
ON c.city_id = d.city_id;''')

queryPrices = """
            INSERT INTO
                apt_prices(adv_id, city_id, price, highlighted, urgent, top_ad, date, update_id)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?); """

queryDetails = """
            INSERT INTO
                apt_details(adv_id, city_id, district_id, region_id,
                title, time_created, time_valid_to, is_business, user_id,
                user_acc_created, latitude, longitude, description, floor,
                furniture, market, builttype, meters, rooms, date)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""


bar = Bar('Running...', max=len(ids), suffix='%(percent)d%%)')
collected_total = 0

for index in range(len(ids)):
    bar.next()
    logger.info(f'getting data for city: {ids[index][0]}, district: {ids[index][1]}')
    # you need different querystring for city with districts and without that's why it's divided into two loops.
    if ids[index][1] is not None:
        # max limit of ads you can access with one request is 50, to access more ads you have to add offset.
        offset = 0
        while True:
            querystring = {"offset": f"{offset}", "limit": "50", "category_id": "14", "city_id": f"{ids[index][0]}",
                           "district_id": f"{ids[index][1]}", "filter_refiners": "", "facets": "[{\"field\":\"city\","
                           "\"fetchLabel\":true,\"fetchUrl\":true,\"limit\":10}]", "sl": "181cea3c35ex24cfd864"}
            start = time.time()
            ads_list = scrap.get_response(querystring)  # list of dicts containing ad details
            size = len(ads_list)
            end = time.time() # to powyrzucać do modułu
            if size == 0:
                break
            logger.info(f'got {size} ads in {end - start} sec')
            for ad in ads_list:
                values = scrap.collect_details(ad)
                values = [int(x) if type(x) is bool else x for x in values]
                priceProm = [values[i] for i in [0, 1, 22, 13, 14, 15]] + [date] + [str(values[0])+date]
                details = values[0:13] + values[16:22] + [date]
                con.insert_data(queryPrices, priceProm)
                con.insert_data(queryDetails, details)
            offset += size
        logger.info(f'Collected details for {offset} ads in city: {ids[index][0]}, district: {ids[index][1]}')
        collected_total += offset
        logger.info(f'Collected {collected_total} so far in total.')
    else:   # sending requests for cities without districts
        offset = 0
        while True:
            priceAll = []
            detailsAll = []
            querystring = {"offset": f"{offset}", "limit": "50", "category_id": "14", "city_id": f"{ids[index][0]}",
                           "filter_refiners": "", "facets": "[{\"field\":\"city\",\"fetchLabel\":true,\"fetchUrl"
                           "\":true,\"limit\":10}]", "sl": "181cea3c35ex24cfd864"}
            start = time.time()
            ads_list = scrap.get_response(querystring)
            size = len(ads_list)
            end = time.time()
            if size == 0:
                break
            logger.info(f'got {size} ads in {end - start} sec')
            for ad in ads_list:
                values = scrap.collect_details(ad)
                values = [int(x) if type(x) is bool else x for x in values]
                priceProm = [values[i] for i in [0, 1, 22, 13, 14, 15]] + [date] + [str(values[0])+date]
                details = values[0:13] + values[16:22] + [date]
                con.insert_data(queryPrices, priceProm)
                con.insert_data(queryDetails, details)
            offset += size
        logger.info(f'Collected details for {offset} ads in city: {ids[index][0]}')
        collected_total += offset
        logger.info(f'Collected {collected_total} so far in total.')
bar.finish()
