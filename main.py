import web3
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/87d6d1a423c54b9888e8cb1bb6ac1b2e"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
balance = web3.eth.getBalance("0x945d8a0d172e1E8B44Aa8F35560CF3AF3E521192")
print(balance)
eth_balance = web3.fromWei(balance, 'ether')
print(eth_balance)

if __name__ == '__main__':
    print("hello")
