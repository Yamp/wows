from http.cookies import SimpleCookie

import scrapy
from scrapy.http import Response
from scrapy.spiders.init import InitSpider

# DOWNLOADER_MIDDLEWARE = [ 'scrapy.contrib.downloadermiddleware.httpauth.HttpAuthMiddleware']
# http_user = "user"
# http_pass = "pass"

# http auth


class ForecastsSpider(InitSpider):
    """Спайдер, который собирает прогнозы от тинькова."""

    name = 'tinkoff_forecasts'
    allowed_domains = ['tinkoff.ru']
    start_urls = ['https://www.tinkoff.ru/invest/feed/?filter=forecasts']
    custom_settings = {}

    # ----------------------------------------------------------------------------------------------------------------
    # Нестандартные штуки
    # ----------------------------------------------------------------------------------------------------------------


    # default_headers = {
    #     "DNT": "1",
    #     "Referer": "https://www.tinkoff.ru/invest/feed/",
    #     "sec-ch-ua": "https://www.tinkoff.ru/invest/feed/",
    #     "sec-ch-ua-mobile": '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    #     "Upgrade-Insecure-Requests": "1",
    #     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    #                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36",
    # }

    # default_cookies = {
    #
    # }

    import requests

    default_headers = {
        'authority': 'www.tinkoff.ru',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.61 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.tinkoff.ru/invest/feed/',
        'accept-language': 'ru-RU,ru;q=0.9',
        'cookie': 'test_cookie_QpHfCYJQhs=true; test_cookie_QpHfCYJQhs=true; __P__wuid=3ccf4e932489ae44e15f9bd606183060; timezone=Europe/Moscow; dsp_click_id=no%20dsp_click_id; ta_uid=1618271788145951157; pageLanding=https%3A%2F%2Fwww.tinkoff.ru%2Finvest%2F; dmp.id=2344dcdd-b4c3-4c50-a7fc-3ca8e1c8720c; prev_page=/invest/; advcake_sid=8f243ae0-b2da-29dd-421a-7c1b3d75bc9d; advcake_trackid=bca9ad2b-ea14-dfab-5650-9031035234ff; AMCVS_A002FFD3544F6F0A0A4C98A5%40AdobeOrg=1; _gcl_au=1.1.638586609.1618271789; s_cc=true; dco.id=76c29c78-ae4e-42d9-ad54-331c69a0cd93; ta_nr=return; ta_visit_num=2; ta_visit_start_ts=1618361913585; __P__wuid_last_update_time=1618361913748; dmp.sid=AWB2PjnGop8; AMCV_A002FFD3544F6F0A0A4C98A5%40AdobeOrg=-1124106680%7CMCIDTS%7C18732%7CMCMID%7C77022918890282323941271474466677847984%7CMCAAMLH-1618966713%7C6%7CMCAAMB-1618966713%7C6G1ynYcLPuiQxYZrsz_pkqfLG9yMXBpb2zX5dvJdYQJzPXImdj0y%7CMCOPTOUT-1618369113s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18737%7CvVersion%7C5.2.0; test_cookie_QpHfCYJQhs=true; utm_date_set=1618362515272; utm_source=id.tinkoff.ru; source=output; _gid=GA1.2.323761015.1618362516; api_session_csrf_token_f53711=ab8c1e9c-982b-4ac1-9d10-a4df45a4167c.1618362618; api_session_csrf_token_c3956a=c9150efe-aca4-4979-a166-559b48443fd3.1618363229; api_session_csrf_token_1478af=f9d66ff5-b367-41c1-aec5-86efea44b50d.1618363842; api_session=JWni174tZAxa8tQaoGcsupwUEnQ1NPT2.m1-prod-api79; api_sso_id=b2e30a4a0db9b0bb4f9237420c5634a1; enabledSharedAuth=true; sso_api_session=t.gYmXoQLSRgpvtAiV8RNDLJ3vjLzGZpLpbqNPYocoeMtvtERQy4cO2hXRJpIif4pkKSbFT6H3c8GVCZhFRKGo4A; psid=JWni174tZAxa8tQaoGcsupwUEnQ1NPT2.m1-prod-api79; pcId=35665256; userType=Client-Heavy; ssoCsrf=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJkZXRhY2hlZF9tb2RlIjpmYWxzZSwicG9zdF9jb21wbGV0ZV9yZWRpcmVjdF91cmkiOiJodHRwczpcL1wvd3d3LnRpbmtvZmYucnVcL2FwaVwvdXNlcnMtbmF2aWdhdGlvblwvY29tbW9uXC9hdXRoXC9jb21wbGV0ZS5odG1sIiwic3RhdGUiOiItYjlFTTNTUnExNnZHT09IYzBtUmNBIiwicmVkaXJlY3RfdXJpIjoiaHR0cHM6XC9cL3d3dy50aW5rb2ZmLnJ1XC9hcGlcL3VzZXJzLW5hdmlnYXRpb25cL2FwaVwvYXV0aG9yaXphdGlvblwvY29tcGxldGU_c3RhdGU9LWI5RU0zU1JxMTZ2R09PSGMwbVJjQSIsImlhdCI6MTYxODM2Mzk1N30.0_1_dWWKZ0i5wVAgwb-pyonekLW0GwcEQCpuXARSFpE; gwSessionID=t.q_H-A8EBN3wfE4_2_TUar1uUoCqAILVnVaUmtWBnU2z6kNfTOoOyqubWCkAdEJ29xEY-2aZxwCE6ECYsjbqLyA; mediaInfo=%7B%22width%22%3A1280%2C%22height%22%3A782%2C%22isTouch%22%3Afalse%2C%22retina%22%3Afalse%2C%22isLandscape%22%3Atrue%7D; _ga=GA1.2.776229890.1618271789; s_sq=%5B%5BB%5D%5D; s_nr=1618364257507-Repeat; _ga_43H68Z69W3=GS1.1.1618361912.2.1.1618364257.54',
    }

    cookie = SimpleCookie()
    cookie.load(default_headers['cookie'])
    default_cookies = {k: v.value for k, v in cookie.items()}

    params = (
        ('filter', 'forecasts'),
    )

    # response = requests.get('https://www.tinkoff.ru/invest/feed/', headers=headers, params=params)

    # NB. Original query string below. It seems impossible to parse and
    # reproduce query strings 100% accurately so the one below is given
    # in case the reproduced version is not "correct".
    # response = requests.get('https://www.tinkoff.ru/invest/feed/?filter=forecasts', headers=headers)

    def __init__(
            self,
            http_user,
            http_pass,
            user_agent,
            *args,
            **kwargs,
    ):
        """Это позволяет передавать параметры."""
        super().__init__(*args, **kwargs)

        self.http_user = http_user
        self.http_pass = http_pass
        self.user_agent = user_agent

    def init_request(self):
        """Авторизация в тинькофф."""

        # return self.initialized()

    def start_requests(self):
        """Начальные запросы.

        Это по сути дефолтная имплементация.
        """
        start_link = 'https://www.tinkoff.ru/invest/broker_account/'


        yield from [
            scrapy.Request(
                url=self.start_urls,
                callback=self.parse,
                method='GET',
                headers=self.default_headers,
                cookies=self.default_cookies,
            )
            for t in self.start_urls
        ]

    def parse(self, response: Response, **kwargs):
        """Парсим страницу. """
        self.logger.info('A response from %s just arrived!', response.url)

        for h3 in response.xpath('//h3').getall():
            yield {'title': h3}

        # for href in response.xpath('//a/@href').getall():
        #     yield scrapy.Request(response.urljoin(href), self.parse)
