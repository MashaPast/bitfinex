import requests
from typing import Union, Dict
import pytest
from bitfinex_API import get_full_url
from logger import appLogger


@pytest.fixture()
def get_response_headers() -> Union[Dict, None]:
    response = requests.get(get_full_url())
    if response.ok:
        headers_data: Dict = dict(response.headers)
        appLogger.debug('Getting response headers from Bitfinex API')
        return headers_data
    else:
        return None


@pytest.fixture()
def get_response_body() -> Union[Dict, None]:
    response = requests.get(get_full_url())
    if response.ok:
        body: Dict = response.json()
        appLogger.debug('Getting response body from Bitfinex API')
        return body
    else:
        return None

