"""Парсим рекоммендации тинькофф."""
import time
from copy import deepcopy
from typing import Literal

import pandas as pd
import requests
from more_itertools import flatten


def download_tinkoff(
        start_cursor: int = 6190000,
        what: Literal["ideas", "forecasts"] = "forecasts",
):
    """Скачиваем штуки из тинькова."""
    headers = {
        'authority': 'www.tinkoff.ru',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'dnt': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': f'https://www.tinkoff.ru/invest/feed/?filter={what}',
        'accept-language': 'ru-RU,ru;q=0.9',
        'cookie': '__P__wuid=3ccf4e932489ae44e15f9bd606183060; timezone=Europe/Moscow;'
                  ' dsp_click_id=no%20dsp_click_id; ta_uid=1618271788145951157;'
                  ' pageLanding=https%3A%2F%2Fwww.tinkoff.ru%2Finvest%2F; dmp.id=2344dcdd-b4c3-4c50-a7fc-3ca8e1c8720c;'
                  ' prev_page=/invest/; advcake_sid=8f243ae0-b2da-29dd-421a-7c1b3d75bc9d;'
                  ' advcake_trackid=bca9ad2b-ea14-dfab-5650-9031035234ff; AMCVS_A002FFD3544F6F0A0A4C98A5%40AdobeOrg=1;'
                  ' _gcl_au=1.1.638586609.1618271789; s_cc=true;'
                  ' dco.id=76c29c78-ae4e-42d9-ad54-331c69a0cd93; ta_nr=return;'
                  ' ta_visit_num=2; ta_visit_start_ts=1618361913585;'
                  ' __P__wuid_last_update_time=1618361913748;'
                  ' dmp.sid=AWB2PjnGop8; test_cookie_QpHfCYJQhs=true;'
                  ' utm_date_set=1618362515272; utm_source=id.tinkoff.ru;'
                  ' source=output; _gid=GA1.2.323761015.1618362516;'
                  ' enabledSharedAuth=true; pcId=35665256;'
                  ' userType=Client-Heavy; api_sso_id=b2e30a4a0db9b0bb4f9237420c5634a1;'
                  ' AMCV_A002FFD3544F6F0A0A4C98A5%40AdobeOrg=-1124106680%7CMCIDTS%7C18732%7CMCMID%7C77022918890282323941271474466677847984%7CMCAAMLH-1618973978%7C6%7CMCAAMB-1618973978%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1618376378s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18737%7CvVersion%7C5.2.0;'
                  ' api_session_csrf_token_76edd6=cfe0dd51-e346-4140-8ec9-3f508688e358.1618370597;'
                  ' api_session=nJMW866YqR7TIhPaSzsdoADLxK3Wkxjf.ds-prod-api67;'
                  ' sso_api_session=t.zkOCIXYbpMkdXR8x8KblQ8foGrbFfo6QwphfsaAxR72qFVuqLGJARBJS_e_YcWfvf8JyCs24vKQPGDb7P-K9SA;'
                  ' psid=nJMW866YqR7TIhPaSzsdoADLxK3Wkxjf.ds-prod-api67;'
                  ' ssoCsrf=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXRhY2hlZF9tb2RlIjpmYWxzZSwicG9zdF9jb21wbGV0ZV9yZWRpcmVjdF91cmkiOiJodHRwczpcL1wvd3d3LnRpbmtvZmYucnVcL2FwaVwvdXNlcnMtbmF2aWdhdGlvblwvY29tbW9uXC9hdXRoXC9jb21wbGV0ZS5odG1sIiwic3RhdGUiOiJUX3lmeUhUcmNzeUFJZm9hUUlhdkJRIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6XC9cL3d3dy50aW5rb2ZmLnJ1XC9hcGlcL3VzZXJzLW5hdmlnYXRpb25cL2FwaVwvYXV0aG9yaXphdGlvblwvY29tcGxldGU_c3RhdGU9VF95ZnlIVHJjc3lBSWZvYVFJYXZCUSIsImlhdCI6MTYxODM3MDYwM30.WaSxjJ0m1nOhD3NJSqT2KgWesTN9NSZHMnnZLp_6cRA;'
                  ' gwSessionID=t.GIlv5KZqpM4Sqmz_xGUVbV3b64OokwJ3iSfFM-j-CPlcyi_FI_YovyCAWXAEc15UhL6fkcUP43TN3K3Tb6NhXw;'
                  ' _ga=GA1.2.776229890.1618271789; _gat_gtag_UA_9110453_3=1;'
                  ' _gat_gtag_UA_9110453_17=1; s_nr=1618371413671-Repeat; s_sq=%5B%5BB%5D%5D;'
                  ' _ga_43H68Z69W3=GS1.1.1618361912.2.1.1618371423.40;'
                  ' mediaInfo={%22width%22:1280%2C%22height%22:782%2C%22isTouch%22:false%2C%22retina%22:false}',
    }

    results = []

    for i in range(6190000, 5700000, -500):
        params = (
            ('sessionId', 'nJMW866YqR7TIhPaSzsdoADLxK3Wkxjf.ds-prod-api67'),
            ('cursor', f'common:1{i:07d}00000000000|personal:-1|social:-1'),
            ('nav_code', 'ideas'),
        )

        response = requests.get('https://www.tinkoff.ru/api/invest/smartfeed-public/v1/feed/api/main', headers=headers,
                                params=params)
        results += [response.json()]
        time.sleep(0.2)
        print(i)


def parse_recommendations(results: list) -> pd.DataFrame:
    """Парсим рекомендации тинькофф."""
    items = flatten([
        r['payload']['items'] if (r['payload']['items'] is not None) else []
        for r in results
    ])

    items = [i['item'] for i in items]
    items = list(items)

    all_data = pd.DataFrame(items)
    all_data = all_data.drop(columns=['logo_name', 'logo_base_color'])
    all_data = all_data.drop_duplicates()

    return all_data


def parse_ideas(results: list) -> pd.DataFrame:
    """Парисм инвестидеи."""
    items = flatten([
        r['payload']['items'] if (r['payload']['items'] is not None) else []
        for r in results
    ])

    items = [i['item'] for i in items]
    items = list(items)

    tickers = []

    for i, it in enumerate(items):
        for t in it['tickers']:
            res = deepcopy(it)
            for k, v in t.items():
                res[k] = v

            res['broker'] = it['broker']['name']
            res['broker_accuracy'] = it['broker']['accuracy']

            tickers += [res]

    all_data = pd.DataFrame(tickers)
    all_data = all_data.drop(columns=['description', 'tags', 'tickers', 'yield'])
    all_data = all_data.drop_duplicates()

    return all_data
