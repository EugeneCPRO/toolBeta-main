
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

    return balances # as string list


# input processed token list, clean tickers
def Tick(ticker):
     
    ticker = str(ticker)
    ticker = re.sub('A-Z0-9', '', ticker)
    ticker = ticker.split(',')
    return ticker # as list 

# input processed balances, clean balances, return float for usage later
def Bal(balance):

    balance = str(balance)
    balance = re.sub('0-9.', '', balance)
    balance = ast.literal_eval(balance)
    balance = list(map(float, balance))

    return balance # as list of floats


# search and cleanup price output, call in loop
def Price(price):

    price = str(price)
    re.sub('0-9.', '', price)
    price = float(price)
    price = round(price, 2)

    return price # as float

# remove unwanted assets
# def valPort(tickers,balances):
#           for token in tickers:
#                if len(token) > 7:
#                     tickers.remove(token)
#                     balances.remove(token)

#                     return tickers, balances
     

# clean portfolio value 
#def Val(value):

#    return value # as float