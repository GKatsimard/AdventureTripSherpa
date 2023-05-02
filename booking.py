import requests
from apikeys import airbnb_api_key, airbnb_api_host

class bookingAPI:

    def __init__(self) -> None:
        self.api_key = airbnb_api_key
        self.api_host = airbnb_api_host