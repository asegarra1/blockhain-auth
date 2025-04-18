from web3 import Web3
import json
import os
import emoji


#file read setups
base_path = os.path.dirname(os.path.abspath(__file__))
contract_address_path = os.path.join(base_path, "contract_address.txt")
device_key_path = os.path.join(base_path, "device_key.txt")
abi_path = os.path.join(base_path, "contract_abi.json")

with open(contract_address_path, "r") as f:
    contract_address = Web3.to_checksum_address(f.read().strip())

with open(device_key_path, "r") as f:
    lines = f.read().strip().splitlines()
    device_address = Web3.to_checksum_address(lines[0].split("=")[1].strip())
    private_key = lines[1].split("=")[1].strip()

with open(abi_path, "r") as f:
    contract_abi = json.load(f)

#connect to ganache(local blockchain)
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("Web3 is not connected to Ganache")

#get contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

#forge tx
nonce = web3.eth.get_transaction_count(device_address)
txn = contract.functions.registerDevice(device_address).build_transaction({
    'chainId': 1337,
    'gas': 200000,
    'gasPrice': web3.to_wei('20', 'gwei'),
    'nonce': nonce
})

signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
txn_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

#helpful user visuals

print("📤 Transaction sent:", web3.to_hex(txn_hash))

receipt = web3.eth.wait_for_transaction_receipt(txn_hash)
print("📬 Transaction confirmed in block:", receipt.blockNumber)

status = contract.functions.isDeviceRegistered(device_address).call()
print("🔐 Device registered:", status)

print("✅ Device has been successfully registered.")
