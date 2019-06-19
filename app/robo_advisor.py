# app/robo_advisor.py
import requests
import json
#import datetime
#currentDT = datetime.datetime.now()

def to_used(my_price):
    return "${0:,.2f}".format(my_price)


#
#INFO INPUTS
#
request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=demo"
response = requests.get(request_url)
#print(type(response))  #class requests.models.response
#print(response.status_code) #200
#print(response.text)  #this is a string and dict

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]

latest_day = "2019-02-20"
latest_close = parsed_response["Time Series (Daily)"][latest_day]["4. close"]


breakpoint()




print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
#print("REQUEST AT: " + str(currentDT.strftime("%Y-%m-%d %H:%M:%S")))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_used(float(latest_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
