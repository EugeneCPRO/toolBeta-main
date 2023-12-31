from aenum import LowerStrEnum
import numpy as np
import urllib3
import pandas
import json
import cleanUp
import time

# unless testnet required, network is always mainnet
network = str("mainnet")
http = urllib3.PoolManager()
url = str("https://rest.cryptoapis.io/v2/blockchain-data/")
mUrl = str("https://rest.cryptoapis.io/market-data/exchange-rates/by-symbols/")


# API call functions
class callAPI(object):
        def __init__(self, chain, network, address):
            self.chain = chain
            self.network = network
            self.address = address

#CryptoAPIs keys
def getHeaders():

    headers = {
    'Content-Type': "application/json",
    'X-API-Key': "02c685e06072bc14c5b75e6ea3e59dd7ffd21b87" # change API key to company 
    }

    return headers

def reqcAPI(chain,address,what,name): # constructors for balance/transaction request URL

    if what == "bal": # for grabbing portfolio
        cBal = str(f'/balance?context={name}') # const balance
        if chain == "ethereum":
            cTok = str(f'/tokens?context={name}&limit=50&offset=0') # const ERC-20 balance

            reqBal = url+chain+"/"+network+"/addresses/"+address+cBal
            reqTok = url+chain+"/"+network+"/addresses/"+address+cTok
            return reqBal, reqTok # return request URLs: L1 bal (e.g. ETH), token bal
        
        reqBal = url+chain+"/"+network+"/addresses/"+address+cBal
        return reqBal
    
    if what == "tx": # for grabbing transactions

        what = str("transactions")
        limit = "&limit=50&offset=0" # transaction limit defaulted to 100
        address = f'/addresses/{address}'
        reqTx = str(f'{url}{chain}/{network}{address}/{what}?context={name}{limit}')
        return reqTx
    
# create data structure of portfolio
def reqJson(rawData):

    data = json.loads(rawData) # convert data to json (works for anything)
    data = pandas.json_normalize([data], max_level=2)
    data = data.T # transpose, data in rows - allows items to be pulled later

    print(data)

    return data

# collect relevant data (tickers & balances)

def processTokens(dec): 

    dec = dec.values.tolist()
    dec = sum(dec,[])

    if len(dec)>4: # function to account for separate L1 token (like ETH)
        balances = cleanUp.getBalances(dec[6])
        tickers = cleanUp.getTickers(dec[6])
    else: # otherwise, collect as normal
        dec = dec[3]
        balances = cleanUp.getBalances(dec)
        tickers = cleanUp.getTickers(dec)

    return tickers, balances

# create tx list from imported app/json
def processTx(dec):
    dec = dec.values.tolist()
    dec = sum(dec,[])
    dec = dec[6]
    return dec
# return lists (ticker, balance) for combined portfolio

def cAPIBal(chain,address,what,name): 

    headers = getHeaders()


    if chain == "ethereum" and what == "bal" :
        reqs = reqcAPI(chain,address,what,name)
        req1 = http.request("GET",reqs[0], headers=headers) # return L1 token balance
        req2 = http.request("GET",reqs[1], headers=headers) # returns other tokens balance
        dec1,dec2 = req1.data.decode("utf-8"),req2.data.decode("utf-8") # decode response

        format1,format2 = reqJson(dec1),reqJson(dec2) # create data structure - L1, Tokens
        format1,format2  = processTokens(format1),processTokens(format2) # make data legible

        # combine ticker/balance lists
        tick1,bal1,tick2,bal2 = format1[0],format1[1],format2[0],format2[1]
        tickers = tick1 + tick2
        balances = bal1 + bal2
        tickers = cleanUp.Tick(tickers)
        balances = cleanUp.Bal(balances)
        return tickers,balances

    elif what == "bal":
    # create request strings
        reqs = reqcAPI(chain,address,what,name)
        reqs = http.request("GET",reqs, headers=headers)
        dec = reqs.data.decode("utf-8")

        format1 = reqJson(dec)
        format1 = processTokens(format1)
        
        tickers,balances = format1[0], format1[1]
        tickers = cleanUp.Tick(tickers)
        balances = cleanUp.Bal(balances)

        return tickers,balances
    


# get transaction data for user wallet
def cAPItx(chain,address,what,name):

    headers = getHeaders()
    reqs = reqcAPI(chain,address,what,name)
    reqs = http.request("GET",reqs, headers=headers)

    # decode response
    dec = reqs.data.decode("utf-8")
    dec = reqJson(dec)
    formatTx = processTx(dec)

    return formatTx

# get price in "base" for "ticker" asset, assign user name to request
def cAPIPrice(ticker,base,name):
    
    now = int(time.time())
    now = str(now)
    tstamp = "Timestamp="+str(now)
    context = f'context={name}&calculation'

    reqUrl = f'{mUrl}{ticker}/{base}?{context}{tstamp}'

    headers = getHeaders()

    # get 
    pReq = http.request("GET", reqUrl, headers = headers)
    dec = pReq.data.decode("utf-8")
    price = reqJson(dec)
    price = pandas.DataFrame.to_numpy(price)
    price = list(price)

    # price is unavailable if index out of range
    try:
        price = price[6][0]
    except IndexError:
        print(f'Price of {ticker}/{base} unavailable!')
        return float(0)
    else:
        return float(price)
    

# get portfolio balance values   
def balValue(portfolio,name):

    base = "usd"
    value = []
    portfolio = np.array(portfolio, dtype=object)
    print(portfolio[0][0], portfolio[1][0])
    for i in range(len(portfolio[0])):
        # i believe this could be optimised by getting all assets with single call
        val = portfolio[1][i] * cAPIPrice(portfolio[0][i],base,name)
        str(val)
        value.append(val)

    total = sum(value)

    return value, total
