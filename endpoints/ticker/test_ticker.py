from helpers.helpers_functions import *
import pytest
import requests

ticker_dict = {'FRR': float, 'BID': float, 'BID_PERIOD': int, 'BID_SIZE': float, 'ASK': float, 'ASK_PERIOD': int, 'ASK_SIZE': float, 'DAILY_CHANGE': float,
'DAILY_CHANGE_RELATIVE': float, 'LAST_PRICE': float, 'VOLUME': float, 'HIGH': float, 'LOW': float, 'FRR_AMOUNT_AVAILABLE': float}


@pytest.mark.parametrize(('symbol'), [('tBTCUSD'), ('fUSD')])
def test_ticker_response(symbol):
    response = requests.get(create_endpoint('ticker/' + str(symbol)))
    start = time.clock()
    response_time = time.clock() - start
    appLogger.debug("Request completed in {}ms".format(response_time))

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)
    write_response_to_a_file(response, "resp_text3.txt")
    # for j in ticker_dict:
    #     for i in range(0, len(body)):
    #         appLogger.debug('Check type' + str(i))
    #         appLogger.debug('Check type' + str(ticker_dict[j]))
    #         field_type = type(body[i])
    #         assert field_type == ticker_dict[j]

    assert response.ok
    assert response_time < 1
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0