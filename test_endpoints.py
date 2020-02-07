from logger import appLogger
import os
from typing import Dict, Union
import json
from endpoints import Endpoint
import requests
import pytest
import time


@pytest.mark.parametrize(('endpoint'), [('platform/status'), ('tickers?symbols=tBTCUSD,tLTCUSD,fUSD'),  ('ticker/tBTCUSD'),
                                        ('trades/fUSD/hist'), ('book/tBTCUSD/P0')])

#('tickers?symbols=tBTCUSD'), ('tickers?symbols=ALL'), ('ticker/fUSD'), ('trades/tBTCUSD/hist'))
def test_response_code_time_content_type(endpoint):
    appLogger.debug('Getting response from 5 endpoints to check response code from Bitfinex API is ok')
    each_endpoint = Endpoint().create_new_endpoint(endpoint)

    start = time.clock()
    response = requests.get(each_endpoint)
    response_time = time.clock() - start
    appLogger.debug("Request completed in {}ms".format(response_time))

    appLogger.debug('Checking asserts for 5 endpoints if response code is ok')
    assert response.ok

    assert response_time < 1

    headers_data: Dict = dict(response.headers)
    appLogger.debug('Getting response headers from Bitfinex API')
    with open(os.path.abspath('assets/content_type.json'), 'r') as f:
        content_type: Dict = json.load(f)
        appLogger.debug('Checking asserts for 5 endpoints if content-type is json')
        assert headers_data['Content-Type'] == content_type['Content-Type']


def test_response_body_field_types_endpoint1():
    each_endpoint = Endpoint().create_new_endpoint('platform/status')
    response = requests.get(each_endpoint)
    body: Dict = response.json()
    appLogger.debug('Getting response body from Bitfinex API')
    print(body[0])
    assert isinstance(body[0], int)


def test_response_body_field_types_endpoint2():
    each_endpoint = Endpoint().create_new_endpoint('tickers?symbols=tBTCUSD,tLTCUSD,fUSD')
    response = requests.get(each_endpoint)
    body: Dict = response.json()
    appLogger.debug('Getting response body from Bitfinex API')
    print(body[0][0])
    assert isinstance(body[0][0], str)
    assert isinstance(body[0][1], float)
    assert isinstance(body[0][2], float)

