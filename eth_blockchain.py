import web3
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/87d6d1a423c54b9888e8cb1bb6ac1b2e"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
latest = web3.eth.blockNumber
print(latest)
print(web3.eth.get_block(latest))

# get the block details
for i in range(0, 10):
    print(web3.eth.get_block(latest - i))

hash='0x0bdd7f5506fc783ecd8455abe93a7870e18ebf5634dd8e35379d871fc644b448'
print(web3.eth.getTransactionByBlock(hash, 2))


