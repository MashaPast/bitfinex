from helpers.helpers_functions import *


def test_platform_status():
    response = make_request(create_endpoint('platform/status'))
    response_time = get_response_time(response)

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)

    assert response.ok
    assert response_time < 300
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0
    assert 0 or 1 in body
