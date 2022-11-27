import json
from web3 import Web3

# in memory blockchain
ganache_url = "HTTP://172.28.16.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# check if connected
print(web3.isConnected())
print(web3.eth.blockNumber)



abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"getGreeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')

address = web3.toChecksumAddress('0x373c266987Bf3Fea8BCC8C4fD6bb33d4bFccCF75')

contract = web3.eth.contract(address=address, abi=abi)

print(contract.functions.getGreeting().call())


# get the first account in the list
web3.eth.defaultAccount = web3.eth.accounts[0]
# write data to the smart contract
# update Greeting
tx_hash = contract.functions.setGreeting("Hello World! (Smart Contract)").transact()
print(tx_hash)

# tx hash
# tx has to be mined
# you want to get a receipt - wait for the receipt
web3.eth.wait_for_transaction_receipt(tx_hash)

print('updated greeting {}'.format(contract.functions.getGreeting().call()))