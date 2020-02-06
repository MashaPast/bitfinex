from logger import appLogger
import os
from typing import Dict
import json


def test_platform_status_body(get_response_body):
    appLogger.debug('Getting headers_asset from file')
    with open(os.path.abspath('assets/platform_status_body.json'), 'r') as f:
        body_asset: Dict = json.load(f)
        appLogger.debug('Checking asserts')
    assert get_response_body == body_asset

