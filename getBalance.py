
import http.client
import requests
import urllib3
import re

# class for portfolio data

class getBalance(object):
    
    def __init__(self, blockchain, address, network):
        self.blockchain = blockchain
        self.address = address
        self.network = network


def getHeaders():
    headers = {
    'Content-Type': "application/json",
    'X-API-Key': "02c685e06072bc14c5b75e6ea3e59dd7ffd21b87" # change API key to company from personal

    }

    return headers

def getData(blockchain, address, network): 

    headers = getHeaders() # grab API Key 

    http = urllib3.PoolManager()

    # grab data for ETH and ERC-20 tokens

    resEth = http.request("GET","https://rest.cryptoapis.io/blockchain-data/"+blockchain+"/"+network+"/addresses/"+address+"/balance?context=yourExampleString", headers=headers)
    resTokens = http.request("GET","https://rest.cryptoapis.io/blockchain-data/"+blockchain+"/"+network+"/addresses/"+address+"/tokens?context=yourExampleString", headers=headers)
    
    ethBalance = resEth.data.decode("utf-8")
    rawTokData = resTokens.data.decode("utf-8")

    # clean up data
    ethBalance = re.sub('[^A-Za-z0-9,:.]', '', ethBalance)
    rawTokData = re.sub('[^A-Za-z0-9,:.]+', '', rawTokData)

    ethBalance = ethBalance.split(",")

    return ethBalance, rawTokData

def getPortfolio(ethBalance, rawTokData):

    # this section sifts through ERC-20 tokens in the wallet and pulls token name, balance

    # break raw data string into a list
    rawTokData = rawTokData.split(',')

    balanceData = []
    tokenData = []

    # scan through raw data and segregate asset from price
    for token in rawTokData:
        if "confirmedBalance" in token: # "confirmedBalance" is the standard syntax for all ETH inputs - need to check for other chains
            token = token.split(':')
            balanceData.append(token[1])

        if "symbol" in token: # "symbol" standard syntax
            token = token.split(':')
            tokenData.append(token[1]) # note that token data includes scam tokens etc. - validation required, will look into later

    # ETH is segregated - this adds it to the total count
    # get ETH balance value and add data to final balances (could be optimised)
    ethBal = []
    for x in ethBalance:

        if "amount" in x:
            x = x.split(':')
            ethBal.append(x[4])

    ethBal = ethBal[0]
    ethBal = re.sub('A-Za-z0-9.', '', ethBal)

    # add ETH data
    tokenData.append("ETH")
    balanceData.append(ethBal)

    return tokenData, balanceData


