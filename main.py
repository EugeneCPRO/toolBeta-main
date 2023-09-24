
import getBalance
import getFinancials
import os


# the code is pretty heavy on API usage - will require more efficient use for scaling

clear = lambda : os.system('tput reset')
clear()

# function for updating prices of BTC ETH (UI example)
def menuPrices():
    btcPrice = getFinancials.getPrice("BTC")
    ethPrice = getFinancials.getPrice("ETH")
    btcPrice = float(btcPrice)
    ethPrice = float(ethPrice)
    return btcPrice, ethPrice

mPrice = menuPrices()

# basic UI example

print(f'  MENU \t\t\t\t BTC Price: ${round(mPrice[0],2)} \t ETH Price: ${round(mPrice[1],2)} \n ___________________ \n \n 1. Ethereum \n \n ___________________\n\n 2. Live price feed \n\n')
choice = input("Choose option: ")
print(" ")

if choice == "1":
    chain = str("ethereum")

elif choice == "2":
    clear()

clear()

print(f'Menu \n ___________________ \n\n1. Use standard address \n')
print("2. Manual input wallet")
print("___________________\n")

choice = input("Choose an option: ")

if choice == "1":
    wallet = str("0x8Be9987d18a10F770cADC94635CeDB2eF33B0f17") # skin in the game wallet

elif choice == "2":
    wallet = input("Paste wallet address: ")
    wallet = str(wallet)
clear()

# grab portfolio statistics
rawData = getBalance.getData(chain,wallet,"mainnet")
portfolio = getBalance.getPortfolio(rawData[0], rawData[1])


# set up vars for balance tracking
ticker = portfolio[0]
balance = portfolio[1]


# function to display portfolio
getFinancials.showPort(ticker,balance)

