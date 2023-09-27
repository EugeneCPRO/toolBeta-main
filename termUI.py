import keyboard
import cleanUp
import itertools


# basic terminal print, will work on better display - potentially to a gSheet (WIP)

# class for printing data

class termUI(object):
        def __init__(self, display):
            self.display = display


# display portfolio
def displayPort(portfolio,portValue,name,chain):

    # initialise
    cleanUp.wipe()
    # remove scam tokens
    portfolio = cleanUp.cleanPort(portfolio)
    tickers = portfolio[0]
    balances = portfolio[1]
    value = portValue[0]
    print(value)

    print(f'\n{name}, {chain} Portfolio Stats')
    print('------------------------------------------')
    print("Asset\t| Balance\t| Value\n-----------------------")

    for a, b, c in zip(tickers, balances, value):
        print(f'{a}\t| {b}\t| ${c}')

    print(f'\n\nTotal value: ${portValue[1]}')

    print ("\nPress Enter to continue...")
    keyboard.wait('enter')

        # call menu function

    return

def displayTransactions(transactions, name, chain):

    import json

    # setup display
    cleanUp.wipe()
    print(f'\n{name}, {chain} Transaction History')
    print('---------------------------------------')
    print(f'{json.dumps(transactions,indent=4)}\n')

    # call menu function


    return 


