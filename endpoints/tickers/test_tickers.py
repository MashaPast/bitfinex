from helpers.helpers_functions import *
import pytest
import requests

tickers_dict = {'SYMBOL': str, 'FRR': float, 'BID': float, 'BID_PERIOD': int, 'BID_SIZE': float, 'ASK': float, 'ASK_PERIOD': int, 'ASK_SIZE': float,
'DAILY_CHANGE': float, 'DAILY_CHANGE_RELATIVE': float, 'LAST_PRICE': float, 'VOLUME': float, 'HIGH': float, 'LOW': float, 'FRR_AMOUNT_AVAILABLE': float}


@pytest.mark.parametrize(('symbols'), [('tBTCUSD'), ('tBTCUSD,tLTCUSD,fUSD'), ('ALL')])
def test_tickers_response(symbols):
    response = requests.get(create_endpoint('tickers?symbols=' + str(symbols)))
    start = time.clock()
    response_time = time.clock() - start
    appLogger.debug("Request completed in {}ms".format(response_time))

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)
    write_response_to_a_file(response, "resp_text4.txt")
    for i in range(0, len(body)):
        for j in range(0, len(body[i])):
            field_type = (type(body[i][j]))
            appLogger.debug('Check type' + str(j))
            assert field_type is float or int

    assert response.ok
    assert response_time < 1
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0