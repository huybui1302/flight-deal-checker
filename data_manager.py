import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_endpoint = "https://api.sheety.co/424012d2e61746fc4e7a466eb4aa202d/flightDeals/prices"

    def get_data(self):
        data = requests.get(url=self.sheety_endpoint)
        return data.json()
