import json
from web3 import Web3

# in memory blockchain
ganache_url = "HTTP://172.25.80.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# check if connected
print(web3.isConnected())
print(web3.eth.blockNumber)

sender_account = "0xD8b2BE965BC55c76A2A566bA530Dc635704CB870"
# to send cryto currency from sender account
# to sign transactions using private key
sender_account_private_key="84fcd53c543b7041e2886fd872377837efce3fee3300e249dfdf843dcf9fa3b0"

receiver_account = "0x69027993d7e64C9Ff96f0594E5274297D7Ba3197"

# get the nance
nonce = web3.eth.getTransactionCount(sender_account)
# build a transaction
tx = {
    # to prevent send transaction twice to eth network
    'nonce': nonce,
    'to': receiver_account,
    'value': web3.toWei(1, 'ether'),
    # some of crypto currency you need to pay when you send a transaction
    # proof of work block chain that has miners on it
    # miners need to be compensated
    'gas': 2000000,
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign the transaction
signed_tx = web3.eth.account.signTransaction(tx, sender_account_private_key)
# send the transactions
# get transaction hash
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(tx_hash))

