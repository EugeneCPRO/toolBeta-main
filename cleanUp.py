
# class for cleaning up strings


import re
import ast


class cleanUp(object):
        def __init__(self, price, balance, value):
            self.price = price
            self.balance = balance
            self.value = value

# clear terminal
def wipe():
    print("\033c",end="")

# list tickers
def getTickers(dec):
        ticker = []
        if len(dec)>4:
            for token in dec:
                token = token.get("symbol")
                ticker.append(token)

        elif 'unit' in dec:
            token = dec.get("unit")
            ticker.append(token)

        return ticker

# input raw token list, extract balances
def getBalances(dec): 
    balances = []
    if len(dec)>4:
        for token in dec:
            token = token.get("confirmedBalance")
            balances.append(token)
 
    else:
        token = dec.get("amount") # L1 tokens only
        balances.append(token)

    balances = Bal(balances)
    return balances # as string list


# input processed token list, clean tickers
def Tick(ticker):

    tkList = []
    for x in ticker:
        ticker = re.sub(",^0-9a-zA-Z", '', x)
        tkList.append(ticker)

    return tkList # as list 

# input processed balances, clean balances, return float for usage later
def Bal(balance):

    balance = str(balance)
    balance = re.sub('0-9.', '', balance)
    balance = ast.literal_eval(balance)
    balance = list(map(float, balance))
    balance = [round(elem,5) for elem in balance] 

    return balance # as list of floats


# search for transactions based on type
# def txSearch(transactions, txType):
#     data = []
#     for search in transactions:
#          search = search.get("")


# search and cleanup price output, call in loop
def Price(price):

    price = str(price)
    re.sub('0-9.', '', price)
    price = float(price)
    price = round(price, 2)

    return price # as float

#remove unwanted assets
def cleanPort(portfolio):
    fTick = []
    upBal = []

    rndBalance = [round(elem,5) for elem in portfolio[1]]
    for i, s in enumerate(portfolio[0]):
        # scam tokens tend to have a space, remove + any 0 balances
        if (' ' not in s or len(s)<7) and rndBalance[i] != 0: 
            fTick.append(s)
            upBal.append(portfolio[1][i])

    cleanPortfolio = fTick,upBal

    return cleanPortfolio


        

