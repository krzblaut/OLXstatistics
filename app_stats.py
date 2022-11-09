from db_con import DbConnect
import logging

# con = DbConnect('{ODBC Driver 17 for SQL Server}', 'DESKTOP-07IDHB4\SQLEXPRESS', 'OLX')
# con.get_connection()

logger = logging.getLogger(__name__)
logging.FileHandler('logfile.log')
logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')


class AppStats:
    """updates data to database used by django app"""
    def __init__(self, db_connection):
        self.con = db_connection

    insert = '''
        INSERT INTO
            OLXstats_stats(stat_id, city_id, date, 
            avg_m2_price_after, avg_unit_price_after, count_after,
            avg_m2_price_primary, avg_unit_price_primary, count_primary,
            avg_m2_price_all, avg_unit_price_all, count_all)
        VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

    def calculate_data(self, date):
        # con = DbConnect('{ODBC Driver 17 for SQL Server}', 'DESKTOP-07IDHB4\SQLEXPRESS', 'OLX')
        # con.get_connection()
        query_base = f"""
                    Select avg_m2=avg(p.price/d.meters), avg_unit=avg(price), count(*)
                    from apt_prices AS p
                    LEFT JOIN apt_details AS d ON p.adv_id = d.adv_id
                    where p.date='{date}'
                    """
        # calculating and inserting data for each city
        city_ids = [1079, 4019, 5659, 7691, 7971, 8959, 10119, 10609, 15241, 16705, 17871, 19701]
        for city in city_ids:
            logger.info(f'Calculating statistics for city {city}')
            prime_after_city = self.con.get_data(query_base + f' AND p.city_id={city} GROUP BY d.market;')
            logger.info('got data from db for primary and aftermarket')
            all_city = self.con.get_data(query_base + f' AND p.city_id={city};')
            logger.info('got data from db for all markets')
            stat_data = [str(city) + str(date)] + [city] + [date]
            city_stats = stat_data + [stat for row in list(prime_after_city) + list(all_city) for stat in row]
            logger.info(f'Inserting statistics for city {city}')
            self.con.insert_data(self.insert, city_stats)

        logger.info(f'Calculating statistics for the whole of Poland')
        prime_after_poland = self.con.get_data(query_base + ' GROUP BY d.market;')
        all_poland = self.con.get_data(query_base)
        stat_data = ['0000' + str(date)] + [0000] + [date]
        city_stats = stat_data + [stat for row in list(prime_after_poland) + list(all_poland) for stat in row]
        logger.info(f'Inserting statistics for the whole of Poland')
        self.con.insert_data(self.insert, city_stats)




