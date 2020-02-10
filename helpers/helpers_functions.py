from config import config_data
from logger import appLogger
from typing import Dict
import os
import json
import requests
import pytest
import time

bitfinex_api_config = config_data['Bitfinex']


def create_endpoint(endpoint_str):
    appLogger.debug('Getting full url for sending request to Bitfinex API')
    full_url = bitfinex_api_config['url'].format(endpoint_str)
    return full_url


def get_response_headers(response_for_headers):
    headers_data: Dict = dict(response_for_headers.headers)
    appLogger.debug('Getting response headers from Bitfinex API')
    return headers_data


def get_json_from_asset(file_path):
    with open(file_path, 'r') as f:
        content_type: Dict = json.load(f)
        appLogger.debug('Getting content type from asset')
        return content_type


def get_response_body(response_for_body):
    body: list = response_for_body.json()
    appLogger.debug('Getting response body from Bitfinex API')
    return body


def write_response_to_a_file(response_data, file_name):
    file = open(file_name, "w")
    file.write(response_data.text)
    file.close()

