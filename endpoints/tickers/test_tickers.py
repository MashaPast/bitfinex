from helpers.helpers_functions import *
import pytest


@pytest.mark.parametrize(('symbols'), LIST_OF_ARGVALUES[0:20]) # ('tBTCUSD'), ('tBTCUSD,tLTCUSD,fUSD'), ('ALL')
def test_tickers_response(symbols):
    response = make_request(create_endpoint('ticker/t' + str(symbols)))
    response_time = get_response_time(response)

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)
    write_response_to_a_file(response, "resp_text4.txt")

    assert response.ok
    assert response_time < 300
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    for i in range(0, len(body)):
    #for j in range(1, len(body[i])):
        field_type = (type(body[i]))
        appLogger.info('Check type' + str(i) + str(field_type))
        assert field_type == int or field_type == float