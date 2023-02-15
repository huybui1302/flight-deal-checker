class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self):
        self.price = 0
        self.duration = 0
        self.arrival_time = 0
        self.departure_time = 0
        self.routes = 0
        self.stop_over = 0
        self.bag_price = {}
        self.link = None
        self.flight_list = []

    def refresh(self):
        self.price = 0
        self.duration = 0
        self.arrival_time = 0
        self.departure_time = 0
        self.routes = 0
        self.stop_over = 0
        self.bag_price = {}
        self.link = None

    def refresh_list(self):
        self.flight_list = []

    def get_data(self, dictionary):
        for item in dictionary['data']:
            self.refresh()
            self.price = f"{item['price']} {dictionary['currency']}"
            for i in item['route']:
                self.routes += 1
                arrival_hour = i['local_arrival'].split("T")[1].split(":")[0]
                arrival_hour_utc = i['utc_arrival'].split("T")[1].split(":")[0]
                # arrival_minute = item.utc_arrival.split("T")[1].split(":")[1]
                departure_hour = i['local_departure'].split("T")[1].split(":")[0]
                departure_hour_utc = i['utc_departure'].split("T")[1].split(":")[0]
                # departure_minute = item.utc_departure.split("T")[1].split(":")[1]
                self.duration += abs(int(arrival_hour_utc) - int(departure_hour_utc))
            self.stop_over = self.routes - 1
            self.bag_price = item['bags_price']
            self.link = dictionary['data'][0]['deep_link']
        self.flight_list.append([self.price, self.duration, self.stop_over, self.bag_price, self.link])
        yield self.flight_list
        self.refresh_list()
