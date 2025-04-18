# 🔐 Pi Blockchain Lock

A Raspberry Pi-powered smart lock simulation that uses **blockchain authentication** to control physical access — no cloud, no vendors, just trustless crypto-based security.

Instead of relying on centralized services like Ring, Nest, or Wi-Fi-based locks, this system uses Ethereum-compatible **challenge-response signing** and **on-chain device registration** to validate access before allowing the LED (simulating a lock) to toggle.

---

## 📦 Features

- 🔑 Challenge-response authentication with ECDSA private key  
- 🔗 Ethereum-style smart contract for access control  
- 📍 Ganache runs locally on the Pi (no internet needed)  
- 💡 Raspberry Pi controls LED via GPIO (lock/unlock simulation)  
- ❌ Unauthorized or unregistered devices are denied access  
- 🧾 Access attempts logged in a local CSV file  

---

## 🛠 Project Structure

| File/Folder              | Description |
|--------------------------|-------------|
| `auth_check.py`          | Runs the lock logic and verifies device via signature |
| `register_device.py`     | Registers a device address on-chain |
| `deregister_device.py`   | Removes device from the smart contract |
| `contract_abi.json`      | Contract ABI (copied from Remix) |
| `contract_address.txt`   | Stores deployed contract address |
| `device_key.txt`         | Contains the device’s Ethereum address and private key |
| `access_log.csv`         | Logs of authentication attempts |
| `DeviceAuth.sol`         | Solidity smart contract code |

---

## 🧱 Hardware Requirements

- Raspberry Pi 3/4/Zero 2 W  
- Breadboard  
- 1x LED  
- 1x Pushbutton  
- 220Ω resistors (optional)  
- Jumper wires  

---

## 🚀 How It Works

1. Deploy a smart contract locally via Remix connected to Ganache  
2. Register the device’s public Ethereum address on-chain  
3. The Pi signs a random challenge using its private key  
4. The signature is verified using the public address  
5. If verified and registered, the LED toggles using the pushbutton  

<img width="465" alt="image" src="https://github.com/user-attachments/assets/f825f68b-3916-496f-9e64-f4d8de594169" />

---

## 🔐 Why Use Blockchain?

- No central server to hack or fail  
- Identity is proven via cryptography  
- Revocation and auditing are native to the chain  
- Real-world simulation of decentralized access control  

---

## ⚙️ Setup Instructions

**Install Python dependencies:**
```
pip3 install web3 eth-account
```

**Install and run Ganache on the Pi:**
```
sudo npm install -g ganache
ganache
```

**Deploy the smart contract:**
1. Open [Remix IDE](https://remix.ethereum.org) on the Pi  
2. Connect to `http://127.0.0.1:8545` (Web3 provider)  
3. Deploy `DeviceAuth.sol`  
4. Save:
   - Contract address → `contract_address.txt`  
   - ABI → `contract_abi.json`  
   - Device address/private key → `device_key.txt`  

---

## 🧪 Run the System

**Register the device:**
```
python3 register_device.py
```

**Start the lock controller:**
```
python3 auth_check.py
```

---

## 🗃 Sample Access Log

Example `access_log.csv` entry:
```
Time: 2025-04-18 14:52:30
Device Address: 0x729643A808Dac1Ef747f0F3dFb596F35c559754a
Transaction ID: 0xabc123...
Auth: SUCCESS
```
 

---

## 🧠 Future Improvements

- Add role-based access control (admin, guest, etc.)  
- Use a secure element to store the private key  
- Migrate to a real Ethereum testnet (e.g., Sepolia)  
- Add a mobile/web frontend dashboard for access management  
- Replace the LED with a solenoid, servo, or real lock  

---

## 👨‍💻 Author

Alexander Segarra
CIS 629 – Blockchain Systems  
Syracuse University

---

## 🛡 License

This project is released under the MIT License — use it, learn from it, build on it.
