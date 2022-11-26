import json
from web3 import Web3

# in memory blockchain
ganache_url = "HTTP://172.18.32.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# check if connected
print(web3.isConnected())
print(web3.eth.blockNumber)

web3.eth.defaultAccount = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"constant":true,"inputs":[],"name":"getGreeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]')
bytecode = '0x608060405234801561001057600080fd5b50600436106100415760003560e01c8063a413686214610046578063ef690cc014610101578063fe50cc7214610184575b600080fd5b6100ff6004803603602081101561005c57600080fd5b810190808035906020019064010000000081111561007957600080fd5b82018360208201111561008b57600080fd5b803590602001918460018302840111640100000000831117156100ad57600080fd5b91908080601f016020809104026020016040519081016040528093929190818152602001838380828437600081840152601f19601f820116905080830192505050505050509192919290505050610207565b005b610109610221565b6040518080602001828103825283818151815260200191508051906020019080838360005b8381101561014957808201518184015260208101905061012e565b50505050905090810190601f1680156101765780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b61018c6102bf565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101cc5780820151818401526020810190506101b1565b50505050905090810190601f1680156101f95780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b806000908051906020019061021d929190610361565b5050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156102b75780601f1061028c576101008083540402835291602001916102b7565b820191906000526020600020905b81548152906001019060200180831161029a57829003601f168201915b505050505081565b606060008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103575780601f1061032c57610100808354040283529160200191610357565b820191906000526020600020905b81548152906001019060200180831161033a57829003601f168201915b5050505050905090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f106103a257805160ff19168380011785556103d0565b828001600101855582156103d0579182015b828111156103cf5782518255916020019190600101906103b4565b5b5090506103dd91906103e1565b5090565b61040391905b808211156103ff5760008160009055506001016103e7565b5090565b9056fea265627a7a72315820f78ea9e926d787ec4f2d0bba5c47ab99df66aba49c89dec5bf05647ba860857864736f6c63430005110032'

Greeter = web3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()
print(tx_hash)