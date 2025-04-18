from web3 import Web3
import json
import os
import emoji
import time
import RPi.GPIO as GPIO
from eth_account import Account
from eth_account.messages import encode_defunct
import csv, datetime

LED_PIN = 17
BUTTON_PIN = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

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

#connect to ganache (blockchain)
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("❌ Web3 is not connected to Ganache")

#get contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

#check if registered
print(f"Checking registration status for device: {device_address}...")
status = contract.functions.isDeviceRegistered(device_address).call()

if not status:
    print("❌ Device is NOT registered.")
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()
    exit()
    

print("✅ Device is REGISTERED on the blockchain.")

def generate_challenge():
    return os.urandom(32)


print("🔍 Checking if device is registered...")
is_registered = contract.functions.isDeviceRegistered(device_address).call()

if not is_registered:
    print("❌ Device is NOT registered. Access denied.")
    GPIO.cleanup()
    exit()

print("✅ Device is registered. Running challenge-response authentication...")

#start Priv. Key verification
challenge = generate_challenge()
message = encode_defunct(challenge)


signed_message = Account.sign_message(message, private_key=private_key)

recovered_addr = Account.recover_message(message, signature=signed_message.signature)

verified = recovered_addr.lower() == device_address.lower()

if not verified:
    print("❌ Authentication failed. Invalid signature.")
    
    with open("authlog.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([
            f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Device Address: {device_address}",
            f"Auth: FAIL"
        ])
    
    GPIO.cleanup()
    exit()

print("✅ Authentication passed! Button control enabled.")


with open("authlog.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow([
        f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"Device Address: {device_address}",
        f"Auth: SUCCESS"
    ])

#button logic
led_on = False
last_press = 0

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:
            now = time.time()
            if now - last_press > 0.4:
                led_on = not led_on
                GPIO.output(LED_PIN, GPIO.HIGH if led_on else GPIO.LOW)
                print("🔆 LED ON" if led_on else "🌑 LED OFF")
                last_press = now
        time.sleep(0.1)

except KeyboardInterrupt:
    print("🛑 Exiting...")
    GPIO.cleanup()

