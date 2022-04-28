class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.duration = 0
        self.routes = 0
        self.stop_over = 0
        self.link = None

    def refresh(self):
        self.price = 0
        self.duration = 0
        self.routes = 0
        self.stop_over = 0
        self.link = None

    def get_data(self, dictionary):
        self.refresh()
        self.price = f"{dictionary['data'][0]['price']} {dictionary['currency']}"
        for item in dictionary['data'][0]['route']:
            self.routes += 1
            arrival_hour = item['utc_arrival'].split("T")[1].split(":")[0]
            # arrival_minute = item.utc_arrival.split("T")[1].split(":")[1]
            departure_hour = item['utc_departure'].split("T")[1].split(":")[0]
            # departure_minute = item.utc_departure.split("T")[1].split(":")[1]
            self.duration += abs(int(arrival_hour) - int(departure_hour))
        self.stop_over = self.routes - 1
        self.link = dictionary['data'][0]['deep_link']
        return [self.price, self.duration, self.stop_over, self.link]
