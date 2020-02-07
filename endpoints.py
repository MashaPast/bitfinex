
class Endpoint:
    def __init__(self):
        self.url: str = 'https://api-pub.bitfinex.com/v2/{}'

    def create_new_endpoint(self, endpoint: str):
        full_url: str = self.url.format(endpoint)
        return full_url

