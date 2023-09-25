import keyboard
import cleanUp
import itertools


# basic terminal print, will work on better display - potentially to a gSheet (WIP)

# class for printing data

class termUI(object):
        def __init__(self, display):
            self.display = display


# display portfolio
def displayPort(portfolio,name,chain):

    # initialise
    cleanUp.wipe()
    tickers = portfolio[0]
    balances = portfolio[1]

    print(f'\n{name}, {chain} Portfolio Stats')
    print('---------------------------------------')


    for a, b in itertools.zip_longest(tickers, balances):
        print(a, b)
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
    print ("\nPress Enter to continue...")
    keyboard.wait('enter')

    # call menu function


    return 


