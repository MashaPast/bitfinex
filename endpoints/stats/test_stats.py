from helpers.helpers_functions import *
import pytest


@pytest.mark.parametrize(('symbol'), ['BTCUSD'])
def test_stats_response(symbol):
    response = make_request(create_endpoint('stats1/pos.size:1m:t' + str(symbol) + ':long/last'))
    response_time = get_response_time(response)

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)
    write_response_to_a_file(response, "resp_text5.txt")

    assert response.ok
    assert response_time < 300
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0

    field_type = check_body_types(body)
    assert field_type == int or field_type == float
