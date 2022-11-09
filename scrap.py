import requests
import time
import random
import time
import logging


logger = logging.getLogger(__name__)
logging.FileHandler('logfile.log')
logging.basicConfig(filename='logfile.log', filemode='w', level=logging.INFO,
                    format='%(asctime)s :: %(levelname)s :: %(name)s :: %(message)s')


class ScrapData:
    """class created for acquiring and handling data from OLX"""

    def __init__(self):
        self.session = requests.Session()
        self.url = "https://www.olx.pl/api/v1/offers"
        self.payload = ""
        self.headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) "
                  "Gecko/20100101 Firefox/102.0",
    "Accept": "*/*",
    "Accept-Language": "pl",
    "Accept-Encoding": "gzip, deflate, br",
    "X-Client": "DESKTOP",
    "X-Device-Id": "2eccca3d-c3e0-4fa8-9457-2dd3e8d9c085",
    "X-Platform-Type": "mobile-html5",
    "Version": "v1.19",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Authorization": "Bearer ab242d50c7e50da27f2b5146e5b99f602862fb78",
    "Referer": "https://www.olx.pl/d/nieruchomosci/mieszkania/sprzedaz/lodzkie/",
    "Connection": "keep-alive",
    "Cookie": "lister_lifecycle=1657029248; onap=181cea3c35ex24cfd864-30-"
              "1821af39911x73e3b14d-48-1658312875; OptanonConsent=isGpcEn"
              "abled=0&datestamp=Wed+Jul+20+2022+11%3A57%3A26+GMT%2B0200+"
              "(Central+European+Summer+Time)&version=6.19.0&isIABGlobal="
              "false&hosts=&genVendors=V9%3A0%2C&consentId=e6981324-1aea-"
              "40c0-8502-68fb74e45d33&interactionCount=1&landingPath=NotL"
              "andingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC000"
              "4%3A1%2Cgad%3A1%2CSTACK42%3A1&geolocation=PL%3B10&Awaiting"
              "Reconsent=false; observed_aui=5832a1116f5d4c0b900c1d32b34d"
              "9d36; dfp_user_id=e1db3f52-59d5-4d6f-a58a-f3886020a732-ver"
              "2; lqstatus=1658311912|1821af39911x73e3b14d|oeu2u-2246#er-"
              "1669||; laquesis=buy-2717@b#cars-31364@a#cars-31875@b#cars"
              "-33524@a#cars-34454@b#edu2r-3360@b#edu2r-3361@b#edu2r-3601"
              "@b#er-1598@b#er-1669@a#er-1697@a#erm-796@a#euonb-524@b#gs-"
              "8410@b#jobs-3722@a#oesx-1770@b#oeu2u-2152@a#oeu2u-2246@b; "
              "laquesisff=a2b-000#aut-716#buy-2279#buy-2489#dat-2874#do-2"
              "963#euonb-114#euonb-48#grw-124#kuna-307#kuna-314#kuna-554#"
              "kuna-603#mou-1052#oesx-1437#oesx-1643#oesx-645#oesx-867#ol"
              "xeu-0000#olxeu-29763#psm-235#psm-308#sd-570#srt-1289#srt-1"
              "346#srt-1434#srt-1593#srt-1758#srt-474#srt-475#srt-683#srt"
              "-899; laquesissu=; OptanonAlertBoxClosed=2022-07-05T13:54:"
              "14.486Z; eupubconsent-v2=CPbqpktPbqpktAcABBENCYCsAP_AAH_AA"
              "AYgI3tf_X__b3_j-_5_f_t0eY1P9_7__-0zjhfdt-8N3f_X_L8X42M7vF3"
              "6pq4KuR4Eu3LBIQdlHOHcTUmw6okVrzPsbk2cr7NKJ7PEmnMbO2dYGH9_n"
              "13TuZKY7_____7z_v-v_v____f_7-3f3__p_3_--_e_V_99zfn9_____9v"
              "P___9v-_9__________34I3gEmGrcQBdiWOBJtGEUKIEYVhIdQKACigGFo"
              "gsIHVwU7K4CfUELABAKgIwIgQYgowYBAAIBAEhEQEgB4IBEARAIAAQAKgE"
              "IACNgEFgBYGAQACgGhYgRQBCBIQZEBEcpgQESJBQT2ViCUHehphCHWWAFA"
              "o_oqEBEoAQLAyEhYOQ4AkBLhZIFmKF8gBGCFAKIAAAA.f_gAD_gAAAAA; "
              "OTAdditionalConsentString=1~89.2008.2072.2322.2465.2501.29"
              "99.3028.3225.3226.3231.3232.3234.3235.3236.3237.3238.3240."
              "3241.3244.3245.3250.3251.3253.3257.3260.3268.3270.3272.328"
              "1.3288.3290.3293.3295.3296.3300.3306.3307.3308.3314.3315.3"
              "316; user_adblock_status=false; _gcl_au=1.1.1921082856.165"
              "7029256; _ga=GA1.1.2023050580.1657029256; __utma=221885126"
              ".2023050580.1657029256.1657029257.1657029257.1; __utmz=221"
              "885126.1657029257.1.1.utmcsr=(direct)|utmccn=(direct)|utmc"
              "md=(none); _ga_V1KE40XCLR=GS1.1.1658309584.5.0.1658309625."
              "19; __gfp_64b=Adhla_6867DYKIj5LtcYQYXnCwOsRkK828ZbhtbR6af.97|1657029262; _hjSessionUser_1685071=eyJpZCI6IjA4Mjk3NmI5LWRjNTAtNWE1Zi05NjkzLWNiODhhZjM5OWQ3NyIsImNyZWF0ZWQiOjE2NTcwMjkyNjQwNzQsImV4aXN0aW5nIjp0cnVlfQ==; __gads=ID=cd6a93842dc004b5-2206da4dc6cd0081:T=1657029266:S=ALNI_Mbn6NTipMDNlL7TTWss8DAtAGOiHQ; cto_bundle=-C-Z9196VUVNcU9NakNZZm80N1pCN2F2TUhLVUNlMzloOWk3bUhtV25EJTJCTmZ4cCUyRkMzQWhOUTlGNVZpZnluNXprZzVJc1IwJTJCQXJzUnFKWDQyJTJGMzVxcHA5M0tPMWQxZHVDOXRTNFMwJTJGQSUyQjFNUzBHZEl0MG9NMVVRbmZYc2NxdXlDTVA5Vw; deviceGUID=2eccca3d-c3e0-4fa8-9457-2dd3e8d9c085; session_start_date=1658312874431; a_access_token=2bfb0374d139a1e689aac5ed41679f9a4930b6cc; a_refresh_token=eac4a926f18eb97e6743f8ad702cce11077cb3fd; a_grant_type=device; user_id=1250197384; user_business_status=private; __gsas=ID=5f7f34263676fd2c:T=1657029316:S=ALNI_Ma-KXfGGJ-9ypP8ei1U3W5zFWVKJQ; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2022-07-20%2009%3A57%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fd%2Fnieruchomosci%2Fmieszkania%2Flodz%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2022-07-20%2009%3A57%3A08%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.olx.pl%2Fd%2Fnieruchomosci%2Fmieszkania%2Flodz%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%3B%20rv%3A102.0%29%20Gecko%2F20100101%20Firefox%2F102.0; sbjs_session=pgs%3D59%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.olx.pl%2Fd%2Fnieruchomosci%2Fmieszkania%2Fsprzedaz%2Flodzkie%2F; ldTd=true; newrelic_cdn_name=CF; PHPSESSID=r6tvgcalscrq4kmgsshhve295p; dfp_segment=%5B%5D; _gid=GA1.2.1680397981.1658309583; _hjSession_1685071=eyJpZCI6IjNiNzMxZDYyLWEzY2MtNGQwNy1iZmExLTNkNzAxZDk2MzBmMiIsImNyZWF0ZWQiOjE2NTgzMDk1ODY5ODgsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; fingerprint=MTI1NzY4MzI5MTs0OzA7MDswOzE7MDswOzA7MDswOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTsxOzE7MTswOzE7MDsxOzA7MDswOzA7MDswOzA7MDswOzE7MTsxOzA7MTswOzA7MDswOzA7MDswOzA7MDswOzA7MDswOzE7MDswOzA7MDswOzA7MDsxOzE7MDswOzA7MTswOzE7MDswOzQwMjk5NjEzNDsxOzI7MjsyOzI7Mjs1OzI4NDgwMDY0MTg7MTM1NzA0MTczODsxOzE7MTsxOzA7MTsxOzE7MTsxOzA7MTsxOzE7MTsxOzE7MDtOYU47MDs0MTAwMjE5OTszNDY5MzA2NTUxOzMxNDE3OTQ2ODE7MTMyMDE5MjI3MDszMDIxMDU5MzM2OzI1NjA7MTA4MDsyNDsyNDsxMjA7NjA7MTIwOzYwOzEyMDs2MDsxMjA7NjA7MTIwOzYwOzEyMDs2MDsxMjA7NjA7MTIwOzYwOzEyMDs2MDsxMjA7NjA7MDswOzA=",
    "TE": "trailers"
}

    def get_response(self, querystr):
        """sends GET request based on provided querystring and returns list of ads details
        the list returned looks like this:
        [
            {'id': 762667243, 'title': 'Mieszkanie, Racibórz ul. Mickiewicza,  pow. użytkowa 56m2, piętro 1', ...},
            {'id': 779582483, 'title': 'Mieszkanie Racibórz ul. Opawska nr 95/6', 'last_refresh_time': '2022-0...},
            {'id': 779498474, 'title': 'Z fajną perspektywą dla młodych!', 'last_refresh_time': '2022-09-04T19...},
            ...
            ]
        """
        start = time.time()
        try:
            response = self.session.request("GET", self.url, data=self.payload, headers=self.headers, params=querystr)
            res = response.json()
        except JSONDecodeError:
            if 'Response' in str(response):
                logger.info('Server error, trying again in 30s')
                time.sleep(30)
                self.get_response(querystr)
        try:
            list_of_ads = res['data']
        except KeyError:
            list_of_ads = []
        end = time.time()
        if len(list_of_ads) > 0: logger.info(f'got {len(list_of_ads)} ads in {end - start} sec')
        return list_of_ads, len(list_of_ads)

    @staticmethod
    def collect_details(det_dict):
        """retrieves data from the list of dictionaries provided by method get_response. Outputs simple, ready to pass
        to database list.
            input:
        {'id': 762667243,
        'url': 'https://www.olx.pl/d/oferta/mieszkanie-raciborz-ul-mickiewicza-pow-uzytkowa-56m2-pietro-1-CID3',
        'title': 'Mieszkanie, Racibórz ul. Mickiewicza,  pow. użytkowa 56m2, piętro 1',
        'last_refresh_time': '2022-09-03T10:43:12+02:00', ... }
            output:
        (762667243, 773, 485, 6, 'Mieszkanie, Racibórz ul. Mickiewicza,  pow. użytkowa 56m2, piętro 1', ... )

          0     1       2           3       4           5               6           7       8           9       10
        (id, city_id, distr_id, region_id, title, time_created, time_valid_to, business, user_id, user_created, lat,
         11    12        13      14       15         16           17       18        19    20   21     22
        lon, desc, highlighted, urgent, top_ad, floor_select, furniture, market, builttype, m, rooms, price)
        """

        parameters = ['floor_select', 'furniture', 'market',
                      'builttype', 'm', 'rooms', 'price']
        details = [det_dict['id'], det_dict["location"]["city"]["id"]]
        try:
            details.append(det_dict["location"]["district"]["id"])
        except KeyError:
            details.append(0)
        details = details + [det_dict["location"]["region"]["id"], det_dict["title"],
                             det_dict['created_time'], det_dict["valid_to_time"],
                             det_dict["business"], det_dict["user"]["id"],
                             det_dict["user"]["created"],
                             det_dict["map"]["lat"], det_dict["map"]["lon"],
                             det_dict["description"].replace('<br />', ''),
                             det_dict["promotion"]["highlighted"], det_dict["promotion"]["urgent"],
                             det_dict["promotion"]["top_ad"]]
        for param in parameters:
            tempparam = 0
            for c in range(len(det_dict['params'])):
                if param in det_dict['params'][c].values():
                    if det_dict['params'][c]['key'] == 'price':
                        tempparam = det_dict['params'][c]['value']['value']
                    else:
                        tempparam = det_dict['params'][c]['value']['key']
            details.append(tempparam)
        return details
