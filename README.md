Decentralized IoT Device Authentication using Blockchain
========================================================

This project demonstrates a secure and decentralized system for registering and verifying IoT devices using Ethereum smart contracts, Web3.py, and a local Ganache blockchain.

--------------------------------------------------------

Project Structure
-----------------

project-root/
|
├── contracts/
│   └── DeviceAuth.sol         --> Solidity smart contract
|
├── python/
│   ├── register_device.py     --> Python script to register one device
│   └── batch_register.py      --> (Coming soon) Script to register multiple devices
|
├── screenshots/               --> Screenshots of demo and setup
├── diagram/                   --> Architecture diagrams
├── final_report/              --> Written project report
└── demo/                      --> Live demo notes or walkthrough

--------------------------------------------------------

How to Run the Demo
-------------------

1. Install Dependencies

- Install Ganache globally:
  npm install -g ganache

- Install Python dependencies:
  pip install web3


2. Start the Local Blockchain

In a terminal, run:
  ganache

This starts a local Ethereum test network at http://127.0.0.1:8545.


3. Deploy the Smart Contract

- Open contracts/DeviceAuth.sol in Remix Desktop
- Set environment to "Web3 Provider"
- Enter RPC URL: http://127.0.0.1:8545
- Deploy the contract
- Copy the deployed contract address and ABI


4. Register a Device with Python

- Edit register_device.py:
  - Paste in the deployed contract address
  - Use one of Ganache's test account addresses and private keys

- Then run the script:
  python python/register_device.py

Expected output:
  Transaction sent. Hash: 0x...
  Transaction confirmed in block: ...
  ✅ Device registered: True

--------------------------------------------------------

What This Project Demonstrates
------------------------------

This project removes the need for centralized device authentication systems.

Each IoT device uses its Ethereum address and private key to register itself on the blockchain via a smart contract. All registration is logged immutably and can be verified without passwords or centralized APIs.

--------------------------------------------------------

Planned Future Features
------------------------

- Batch registration of multiple devices with logging
- Device revocation support
- Raspberry Pi hardware simulation
- Deployment to Ethereum testnet (e.g., Sepolia)
- Dashboard or visual front-end for checking registration status

--------------------------------------------------------

Author
------

Alexander Segarra

--------------------------------------------------------

License
-------

MIT License – for educational and demonstration purposes.
