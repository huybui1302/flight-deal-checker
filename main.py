from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from customer_acquisition import CustomerInfo

historic = DataManager()
search = FlightSearch()
raw_data = FlightData()
email = NotificationManager()
info = CustomerInfo()
email_list = info.get_info()
print(email_list)
lowest = historic.get_data()
message = ""


for item in lowest["prices"]:
    destination = item["city"]
    destination_code = item["iataCode"]
    price = item["lowestPrice"]
    results = search.search_flight(destination_code, price)
    if results["_results"] == 0:
        pass
    else:
        processed_data = raw_data.get_data(results)
        message += f"Destination: {destination}\nPrice: {processed_data[0]}\n" \
                   f"Flight duration: {processed_data[1]} hours\nNumber of stop overs: {processed_data[2]}\n" \
                   f"Link: {processed_data[3]}\n\n"
if len(message) > 1:
    for _ in email_list:
        email.send_email(_, message)
        print(message)
