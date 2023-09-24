
import http.client
import requests
import urllib3
import re
import time
import getBalance

# class for financial data

class getFinancials(object):
    
    def __init__(self, tokenData):
        self.tokenData = tokenData

# grab price from API
def getPrice(tokenData):
    #/market-data/exchange-rates/by-symbols/btc/usd?context=yourExampleString&calculationTimestamp=1635514425
    
    headers = getBalance.getHeaders()
    token = tokenData

    # create live timestamp, plugs into API URL
    now = int(time.time())
    now = str(now)
    tstamp = "Timestamp="+str(now)

    http = urllib3.PoolManager()

    # grab API price data
    resPrice = http.request("GET","https://rest.cryptoapis.io/market-data/exchange-rates/by-symbols/"+token+"/usdt?context=yourExampleString&calculation"+tstamp, headers=headers)
    price = resPrice.data.decode("utf-8")
    
    # cleanup and split
    
    price = re.sub('[^A-Za-z0-9,:.]', '', price)
    price = price.split(',')

    usdValue = []

    # extract USD value from string
    for usdt in price:

        if "rate" in usdt: # "rate" is the standard syntax for all price calls - need to check for other chains
            usdt = usdt.split(':')
            usdValue.append(usdt[1])
 
    # remove unwanted characters
    price = usdValue
    price = re.sub('A-Za-z0-9.', '', price)
    price = float(price)

    return price

# update portfolio value 
def getValue(ticker,balance,price):

    for x in range(len(ticker)):
        tick = str(ticker[x]) # temp data
        bal = float(balance[x])
        price = getPrice(tick) # get price for x asset
        value = bal * price # calculate asset holdings in $
        value = str(value) # return string

# function to display portfolio
def showPort(ticker,balance):
    print(f' Assets \t | Balance \t | Value')
    for x in range(len(ticker)):
        tick = ticker[x]
        bal = balance[x]
        balFloat = float(bal)
        price = getPrice(tick)
        price = float(price)
        value = price * balFloat
        print(f'{tick} \t : {bal} \t ${value}')

    return value
    

