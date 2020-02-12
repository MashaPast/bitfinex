from helpers.helpers_functions import *
import pytest


@pytest.mark.parametrize(('symbol'), [LIST_OF_ARGVALUES[0]])
def test_ticker_response(symbol):
    response = make_request(create_endpoint('ticker/t' + str(symbol)))
    response_time = get_response_time(response)

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)
    write_response_to_a_file(response, "resp_text3.txt")
    for i in range(0, len(body)):
        field_type = (type(body[i]))
        appLogger.info('Check type ' + str(i) + str(field_type))
        assert field_type == int or field_type == float

    assert response.ok
    assert response_time < 300
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0
