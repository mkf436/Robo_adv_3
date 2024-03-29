# app/robo_advisor.py
import csv
import requests
import json
import os

from dotenv import load_dotenv

load_dotenv()
import datetime
currentDT = datetime.datetime.now()

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


#
#INFO INPUTS
#
api_key = os.environ.get("ALPHAVANTAGE_API_KEY")
#print(api_key)
symbol = input("ENTER STOCK TICKER: ")

 #TODO:accept user input
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"
response = requests.get(request_url)
#print(type(response))  #class requests.models.response
#print(response.status_code) #200
#print(response.text)  #this is a string and dict

parsed_response = json.loads(response.text)
last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]


#breakpoint

tsd = parsed_response["Time Series (Daily)"]
dates = list(tsd.keys())

latest_day = dates[0]
latest_close = tsd[latest_day]["4. close"]


high_prices = []
low_prices = []

for date in dates:
    high_price = tsd[date]["2. high"]
    low_price = tsd[date]["3. low"]
    high_prices.append(float(high_price))
    low_prices.append(float(low_price))

#get high price from each day
#high_prices = [10, 20, 30, 5]
#max of all the high prices
recent_high = max(high_prices)
recent_low = min(low_prices)

#csv_file_path = "data/prices.csv" # a relative filepath

csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "prices.csv")

csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]
with open(csv_file_path, "w") as csv_file: # "w" means "open the file for writing"
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader() # uses fieldnames set above
    for date in dates:
        daily_prices = tsd[date]
        writer.writerow({
            "timestamp": date,
            "open": daily_prices["1. open"],
            "high": daily_prices["2. high"],
            "low": daily_prices["3. low"],
            "close": daily_prices["4. close"],
            "volume": daily_prices["5. volume"],
            })

#if recommendation:
#    float(latest_close) > 1.2*(recent_low):
#    print("BUY!")
#else:
#    print("DON'T BUY!")

recommendation = "MAYBE BUY?"
reason = "NO GOOD REASON"

print("-------------------------")

print(f"SELECTED SYMBOL: {symbol}")

print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: " + str(currentDT))
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(latest_close))}")
print(f"RECENT HIGH: {to_usd(float(recent_high))}")
print(f"RECENT LOW: {to_usd(float(recent_low))}")
print("-------------------------")

if recommendation:
    float(latest_close) > 1.2*(recent_low)
    print("RECOMMENDATION: BUY!")
else:
    print("RECOMMENDATION: DON'T BUY!")

if reason:
    float(latest_close) > 1.2*(recent_low)
    print("REASON: STOCK CLOSED MORE THAN 20% ABOVE RECENT LOW")
else:
    print("REASON: STOCK CLOSED LESS THAN 20% ABOVE RECENT LOW")

print(f"RECOMMENDATION REASON: {reason}")

print("-------------------------")
print(f"WRITING DATA TO CSV: {csv_file_path}...")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
