import json

from aenum import LowerStrEnum
import cleanUp
import callAPI
import termUI
import GUI
import dataBase

cleanUp.wipe()
#GUI.main_Menu()

# test inputs - will be part of menus
chain = str("bitcoin")
address = str("bc1qzpppmek8wh2vqymq06petmfwmhjj9k8vdxl389")
what = str("bal") # tx = transactions, bal = balances
name = str("SITG")

#construct filename/check if file exists
filename = dataBase.consFileName(name,what,chain)
print(filename)

# update portfolio 
def getPortfolio(filename,chain,address,what,name):
    portfolio = callAPI.cAPIBal(chain,address,what,name)
    portfolio = cleanUp.cleanPort(portfolio)
    dataBase.writeTo(filename, portfolio)
    return portfolio

# display portfolio
def showPortfolio():
    # check if portfolio exists in database
    portfolio = dataBase.readFrom(filename)

    if not portfolio:
        portfolio = getPortfolio(filename,chain,address,what,name)
    
    portValue = callAPI.balValue(portfolio, name) # returns balance values & total
    termUI.displayPort(portfolio,portValue,name,chain)

# get transactions
def showTransactions(filename):
    #transactions = callAPI.cAPItx(chain,address,what,name) # from API
    transactions = dataBase.readFrom(filename) # from file
    termUI.displayTransactions(transactions, name, chain)

def showPrice():
    price = callAPI.cAPIPrice("BTC", "usdt", name)
    print(price)

def getPrice(ticker,base,name):
    ticker = ticker.upper()
    base = base.lower()
    price = callAPI.cAPIPrice(ticker,base,name)
    print(f'The price of {ticker} is ${price}')

#getPrice("THOR","RUNE","Eugene")

showPortfolio()



