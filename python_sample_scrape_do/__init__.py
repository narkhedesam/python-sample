"""
    Date: 29-08-2020
    Created by Sameer Narkhede
    Project : python_sample
    Module : python_sample_scrape_do
"""
import traceback
import requests


class Scrape_do_Exception(BaseException):
    """
    custom Scrape.do exception class
    """
    pass


class python_sample:
    """
    Python sample class for proxy rotating api's https://scrape.do
    """

    def __init__(self):
        self.scrape_do_api_token = None

    def set_api_token(self, api_token=None):
        """
        set scrape.do api token you can find this token from https://scrape.do/dashboard this needs login.
        :param api_token: String API_TOKEN from https://scrape.do
        :return: None
        """
        self.scrape_do_api_token = api_token

    def account_status(self):
        """
        returns the statistics of your scrape.do account
        :return: Dictionary of statistics
        """
        if self.scrape_do_api_token:

            response = requests.get("http://api.scrape.do/info?token=" + self.scrape_do_api_token)

            return response.json()
        else:
            raise Scrape_do_Exception("api-token is not configured")

    def create_request_url(self, url, method="GET", payload=None, headers=None, render=False,
                           super_proxies=False, geo_code=None):
        """
        Best Rotating Proxy & Scraping API Alternative https://scrape.do/ api handler
        new request url

        :param url: String the url user needs to scrape. Ex. 'https://httpbin.org/get'

        :param method: String method for the url request. Ex. ``GET``, ``OPTIONS``, ``HEAD``, ``POST``, ``PUT``,
                        ``PATCH``, or ``DELETE``

        :param payload: (optional) Dictionary, list of tuples, bytes, or file-like object to send in the body of the

        :param headers: (optional) Dictionary of HTTP Headers to send with the request

        :param render: (optional) Boolean - To use Javascript, all you need to do is setting render parameter to true
                        ** Beware that you need a business plan to use this feature!

        :param super_proxies:(optional) Boolean - To use Super Proxies, all you need to do is setting super parameter
                            to true
                        ** Beware that you need a business plan to use this feature!
        :param geo_code: geocode in 'us', 'gb', 'ca', 'tr', 'cn', 'ru', 'se', 'de', 'fr', 'es', 'br' ex. us
                        ** Beware that you need a Pro plan to use this feature!

        :return: response of scrape.do api

        """

        # check if there is token is configured
        if self.scrape_do_api_token:
            base_url = "http://api.scrape.do"

            params = {'token': self.scrape_do_api_token}

            if headers is None:
                headers = {}

            if payload is None:
                payload = {}

            if headers is not None and headers is not {}:
                params['customHeaders'] = 'true'

            params['url'] = url

            if render:
                params['render'] = 'true' if render else 'false'

            if super_proxies:
                params['super'] = 'true' if super_proxies else 'false'

            if geo_code:
                geocodes = ['us', 'gb', 'ca', 'tr', 'cn', 'ru', 'se', 'de', 'fr', 'es', 'br']

                if geo_code not in geocodes:
                    raise Scrape_do_Exception(
                        "Geo-Code is not valid. please provide geo-code in " + str(geocodes))

                params['geo_code'] = geo_code

            methods = ["GET", "OPTIONS", "HEAD", "POST", "PUT", "PATCH", "DELETE"]
            if method not in methods:
                raise Scrape_do_Exception("method is not valid. please provide method in " + str(methods))

            response = requests.request(method, base_url, params=params, headers=headers, data=payload)

            print("status_code:" + str(response.status_code))

            if response.status_code == 200:
                return response.text.encode('utf8')

            elif response.status_code == 404:
                raise Scrape_do_Exception("Target url not found :: Pass valid URL")

            elif response.status_code == 429:
                raise Scrape_do_Exception("You are sending too many concurrent request :: Please upgrade your "
                                          "plan or contact with sale.")

            elif response.status_code == 401:
                raise Scrape_do_Exception("You have not credit :: Please upgrade your plan or contact with sale.")

            elif response.status_code == 502:
                raise Scrape_do_Exception("Gateway Error :: Please retry and check response. If you live "
                                          "constantly, contact support@scrape.do")

        else:
            raise Scrape_do_Exception("api-token is not configured")


if __name__ == '__main__':

    API_TOKEN = "Your_API_TOKEN_FOR_scrape.do"

    # create an python-sample object
    sample = python_sample()

    # set the scrape.do api key
    # sample.set_api_token(api_token=API_TOKEN)

    # Get Scrape.do account statistics
    try:
        resp = sample.account_status()
        print("Response Type " + str(type(resp)))
        print(resp)
    except ConnectionError as e:
        print(str(e))
        print(traceback.format_exc())

    except Scrape_do_Exception as e:
        print(str(e))
        print(traceback.format_exc())

    try:
        resp = sample.create_request_url(url='https://docs.scrape.do/', method="GET", payload={}, headers={},
                                         render=False, super_proxies=False, geo_code=None)
        print(resp)
    except ConnectionError as e:
        print(str(e))
        print(traceback.format_exc())

    except Scrape_do_Exception as e:
        print(str(e))
        print(traceback.format_exc())
