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
chain = str("ethereum")
address = str("0x8Be9987d18a10F770cADC94635CeDB2eF33B0f17")
what = str("bal") # tx = transactions, bal = balances
name = str("SITG")
filename = str("sampletxOutput.json")


# display portfolio
def showPortfolio():
    portfolio = callAPI.cAPIBal(chain,address,what,name) # get balances 
    portValue = callAPI.balValue(portfolio, name) # returns balance values & total

    termUI.displayPort(portfolio,portValue,name,chain)

# get transactions
def showTransactions():
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

getPrice("THOR","RUNE","Eugene")

#showPortfolio()



