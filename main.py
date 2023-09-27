
import json
import cleanUp
import callAPI
import termUI
import dataBase

cleanUp.wipe()
#GUI.main_Menu()

# test inputs - will be part of menus
chain = str("ethereum")
address = str("0x8Be9987d18a10F770cADC94635CeDB2eF33B0f17")
what = str("bal") # tx = transactions, bal = balances
name = str("SITG")

#construct filename/check if file exists
userPath = dataBase.consFileName(name,what,chain)
print(userPath)

# update portfolio 
def getPortfolio(userPath,chain,address,what,name):
    portfolio = callAPI.cAPIBal(chain,address,what,name)
    portfolio = cleanUp.cleanPort(portfolio)
    dataBase.writeTo(userPath, portfolio)
    return portfolio

# display chain specific portfolio
def showChainPortfolio(chain):
    # check if portfolio exists in database
    portfolio = dataBase.readFrom(userPath)

    if not portfolio:
        portfolio = getPortfolio(userPath,chain,address,what,name)

    #clean loaded portfolio
    portfolio = cleanUp.Tick(portfolio[0]), cleanUp.Bal(portfolio[1])
    # returns balance values & total, lighter on API
    portValue = callAPI.balValue(portfolio, name) 

    termUI.displayPort(portfolio,portValue,name,chain)

# show total balances
def showPortfolio():
    return


def getTransactions(userPath,chain,address,what,name):
    transactions = callAPI.cAPItx(chain,address,what,name)
    dataBase.writeTo(userPath, transactions)
    return transactions


# get transactions
def showTransactions():
    transactions = dataBase.readFrom(userPath) # from file
    if not transactions:
        transactions = getTransactions(userPath,chain,address,what,name)
        
    termUI.displayTransactions(transactions, name, chain)



def showPrice():
    price = callAPI.cAPIPrice("BTC", "usdt", name)
    print(price)

def getPrice(ticker,base,name):
    ticker = ticker.upper()
    base = base.lower()
    price = callAPI.cAPIPrice(ticker,base,name)
    print(f'The price of {ticker} is ${price}')


#showTransactions()

showChainPortfolio()





