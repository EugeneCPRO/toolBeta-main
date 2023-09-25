import json
import cleanUp
import itertools

# class for printing data

class termUI(object):
        def __init__(self, display):
            self.display = display


def displayPort(portfolio,name,chain):
      
    cleanUp.wipe()
    tickers = portfolio[0]
    balances = portfolio[1]

    # set up display
    print(f'\n{name}, {chain} Portfolio Stats')
    print('---------------------------------------')


    for a, b in itertools.zip_longest(tickers, balances):
        print(a, b)

    return

def displayTransactions(transactions, name, chain):
     
    # setup display
    cleanUp.wipe()
    print(f'\n{name}, {chain} Transaction History')
    print('---------------------------------------')
    print(json.dumps(transactions,indent=4))

    return 


