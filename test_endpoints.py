from logger import appLogger
import os
from typing import Dict
import json
from endpoints import Endpoint
import requests
import pytest
import time


@pytest.mark.parametrize(('endpoint'), [('platform/status'), ('tickers?symbols=tBTCUSD,tLTCUSD,fUSD'),  ('ticker/tBTCUSD'),
                                        ('trades/fUSD/hist'), ('book/tBTCUSD/P0')])

#('tickers?symbols=tBTCUSD'), ('tickers?symbols=ALL'), ('ticker/fUSD'), ('trades/tBTCUSD/hist'))
def test_response_code_time_content_type(endpoint):
    appLogger.debug('Getting response to check if response code from Bitfinex API is ok')
    each_endpoint = Endpoint().create_new_endpoint(endpoint)

    start = time.clock()
    response = requests.get(each_endpoint)
    response_time = time.clock() - start
    appLogger.debug("Request completed in {}ms".format(response_time))

    appLogger.debug('Check if response code is ok')
    assert response.ok

    assert response_time < 1

    headers_data: Dict = dict(response.headers)
    appLogger.debug('Getting response headers from Bitfinex API')
    with open(os.path.abspath('assets/content_type.json'), 'r') as f:
        content_type: Dict = json.load(f)
        appLogger.debug('Check if content-type is json')
        assert headers_data['Content-Type'] == content_type['Content-Type']

    body: list = response.json()
    appLogger.debug('Check if response type is list')
    assert isinstance(body, list)

def write_response_to_a_file(response_data, file_name):
    file = open(file_name, "w")
    file.write(response_data.text)
    file.close()


def test_response_body_field_types_endpoint1():
    each_endpoint = Endpoint().create_new_endpoint('platform/status')
    response = requests.get(each_endpoint)
    body: list = response.json()
    appLogger.debug('Writing response body to a file')
    write_response_to_a_file(response, "resp_text1.txt")
    appLogger.debug('Getting response body from Bitfinex API')
    assert isinstance(body[0], int)


def test_response_body_field_types_endpoint2():
    each_endpoint = Endpoint().create_new_endpoint('tickers?symbols=tBTCUSD')
    response = requests.get(each_endpoint)
    body: list = response.json()
    #list_of_types = [str, float, float, str, float, float, str, float, float, str, float, float]
    appLogger.debug('Writing response body to a file')
    write_response_to_a_file(response, "resp_text2.txt")
    for i in range(0, len(body)):
        for j in range(0, len(body[i])):
            a = (type(body[i][j]))
            appLogger.debug('Check type')
            assert a is str
    # assert isinstance(body[0][0], str)
    # assert isinstance(body[0][1], float)
    # assert isinstance(body[0][2], float)

