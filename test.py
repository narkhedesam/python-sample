"""
    Date: 29-08-2020
    Created by Sameer Narkhede
    Project : python_sample
"""
import traceback

from python_sample_scrape_do import Scrape_do_Exception, python_sample


API_TOKEN = "Your_API_TOKEN_FOR_scrape.do"

# create an web scrapper object
sample = python_sample()

# set the scrape.do api key
sample.set_api_token(api_token=API_TOKEN)

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

