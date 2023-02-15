import requests
from flight_data import FlightData
from datetime import *

HOME = "YUL"
DESTINATION = "SGN"
# DATE_FROM = date.today().strftime("%d/%m/%Y")
# DATE_TO = (date.today() + timedelta(days=7)).strftime("%d/%m/%Y")
DATE_FROM = "03/08/2023"
DATE_TO = "17/08/2023"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.tequila_endpoint = "http://tequila-api.kiwi.com/v2/search"
        # self.today = date.today()
        # self.seven_days_from_now = self.today + timedelta(days=7)
        self.parameters = {
            "fly_from": HOME,
            "fly_to": "",
            "price_to": "",
            "curr": "CAD",
            "max_stopovers": 2,
            "sort": "price",
            "limit": 10,
            "date_from": DATE_FROM,
            "date_to": DATE_TO,
        }
        self.headers = {
            "apikey": "lUGsr4ret_idQLtf7p7uAUj98A8ODlUy"
        }

    def search_flight(self, destination, price):
        self.parameters["fly_to"] = destination
        self.parameters["price_to"] = price
        search = requests.get(url=self.tequila_endpoint, params=self.parameters, headers=self.headers)
        # print(search.json())
        return search.json()


s = FlightSearch()
raw_data = FlightData()
results = s.search_flight(DESTINATION, "")
if results["_results"] == 0:
    pass
else:
    processed_data = raw_data.get_data(results)
    for item in processed_data:
        print(item)
