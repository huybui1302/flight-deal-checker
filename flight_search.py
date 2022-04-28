import requests
from datetime import *

HOME = "YUL"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_endpoint = "http://tequila-api.kiwi.com/v2/search"
        self.today = date.today()
        self.seven_days_from_now = self.today + timedelta(days=7)
        self.parameters = {
            "fly_from": HOME,
            "fly_to": "",
            "price_to": "",
            "curr": "CAD",
            "max_stopovers": 2,
            "sort": "price",
            "limit": 1,
            "date_from": self.today.strftime("%d/%m/%Y"),
            "date_to": self.seven_days_from_now.strftime("%d/%m/%Y"),
        }
        self.headers = {
            "apikey": "lUGsr4ret_idQLtf7p7uAUj98A8ODlUy"
        }

    def search_flight(self, destination, price):
        self.parameters["fly_to"] = destination
        self.parameters["price_to"] = price
        search = requests.get(url=self.tequila_endpoint, params=self.parameters, headers=self.headers)
        print(search.json())
        return search.json()
