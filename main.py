import json
import cleanUp
import callAPI
import termUI
import GUI

chain = str("ethereum")
address = str("0x8Be9987d18a10F770cADC94635CeDB2eF33B0f17")
what = str("tx")
name = str("Skin in the Game")

with open('sampletxOutput.json')as file:

    transactions = file.read()

transactions = json.loads(transactions)

cleanUp.wipe()

# chain = input("Enter chain (default ethereum = 1): ")
# address = input("Enter address (default SITG = 1): ")
# what = input("Enter operation (default get balance = 1): ")
# name = input("Enter your name: ")

# grab portfolio stats
#portfolio = callAPI.cAPIBal(what,name,chain,address)


# display portfolio
#termUI.displayPort(portfolio,name,chain)

# get transactions
# transactions = callAPI.cAPItx(chain,address,what,name)
termUI.displayTransactions(transactions, name, chain)

#GUI.main_Menu()