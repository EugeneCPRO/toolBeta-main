import json
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
what = str("tx")
name = str("Skin in the Game")
filename = str("sampletxOutput.json")

# grab portfolio stats
#portfolio = callAPI.cAPIBal(what,name,chain,address)

# display portfolio
#termUI.displayPort(portfolio,name,chain)

# get transactions
# transactions = callAPI.cAPItx(chain,address,what,name) # from API
transactions = dataBase.readFrom(filename) # from file

# display tx
termUI.displayTransactions(transactions, name, chain)

#GUI.main_Menu()