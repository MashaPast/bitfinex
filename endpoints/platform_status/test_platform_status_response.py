from helpers.helpers_functions import *

response = requests.get(create_endpoint('platform/status'))


def test_platform_status():
    start = time.clock()
    response_time = time.clock() - start
    appLogger.debug("Request completed in {}ms".format(response_time))

    headers_data = get_response_headers(response)
    content_type = get_json_from_asset(os.path.abspath('assets/content_type.json'))
    body = get_response_body(response)

    assert response.ok
    assert response_time < 1
    assert headers_data['Content-Type'] == content_type['Content-Type']
    assert isinstance(body, list)  # not empty
    assert len(body) != 0
    assert 0 or 1 in body
