from datetime import date
from db_con import DbConnect

con = DbConnect('{ODBC Driver 17 for SQL Server}', 'DESKTOP-07IDHB4\SQLEXPRESS', 'OLX')
con.get_connection()

date = str(date.today())
ids = [1079, 4019, 5659, 7691, 7971, 8959, 10119, 10609, 15241, 16705, 17871, 19701]

query_insert = '''
            INSERT INTO
                OLXstats_stats(stat_id, city_id, date, avg_m2_price_primary, avg_m2_price_after, 
                avg_m2_price_all, avg_unit_price_primary, avg_unit_price_after, avg_unit_price_all, 
                count_primary, count_after, count_all)
            VALUES
                (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
'''

# stats for certain cities
for city in ids:
    query_prime_after = f'''
    Select d.market, avg_m2=avg(p.price/d.meters), avg_unit=avg(price), count(*)
    from apt_prices AS p
    LEFT JOIN apt_details AS d ON p.adv_id = d.adv_id
    where p.city_id={city} AND p.date='{date}'
    GROUP BY d.market;
    '''

    query_all = f"""
    Select avg_m2=avg(p.price/d.meters), avg_unit=avg(price), count(*)
    from apt_prices AS p
    LEFT JOIN apt_details AS d ON p.adv_id = d.adv_id
    where p.city_id={city} AND p.date='{date}';
    """

    adv_div = con.get_data(query_prime_after)
    adv_all = con.get_data(query_all)
    print(adv_all)
    print(adv_div)
    city_stats = []
    city_stats = [str(city)+str(date)] + [city] + [date] + [adv_div[1][1]] + [adv_div[0][1]] + [adv_all[0][0]]
    city_stats += [adv_div[1][2]] + [adv_div[0][2]] + [adv_all[0][1]]
    city_stats += [adv_div[1][3]] + [adv_div[0][3]] + [adv_all[0][2]]
    con.insert_data(query_insert, city_stats)

# stats for whole of Poland

query_prime_after = f'''
Select d.market, avg_m2=avg(p.price/d.meters), avg_unit=avg(price), count(*)
from apt_prices AS p
LEFT JOIN apt_details AS d ON p.adv_id = d.adv_id
where p.date='{date}'
GROUP BY d.market;
'''
query_all = f"""
Select avg_m2=avg(p.price/d.meters), avg_unit=avg(price), count(*)
from apt_prices AS p
LEFT JOIN apt_details AS d ON p.adv_id = d.adv_id
where p.date='{date}';
"""
adv_div = con.get_data(query_prime_after)
adv_all = con.get_data(query_all)
city_stats = []
city_stats = ['0000' + str(date)] + [0000] + [date] + [adv_div[1][1]] + [adv_div[0][1]] + [adv_all[0][0]] + [
    adv_div[1][2]] + [adv_div[0][2]] + [adv_all[0][1]] + [adv_div[1][3]] + [adv_div[0][3]] + [adv_all[0][2]]
con.insert_data(query_insert, city_stats)


