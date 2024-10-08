import time
from web3 import Web3
from dotenv import load_dotenv
import os
from eth_account import Account

# Load environment variables
load_dotenv()

# Assign variables from .env
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
RECIPIENT_WALLET = os.getenv('RECIPIENT_WALLET')
INFURA_URL = os.getenv('INFURA_URL')

# Derive the public address from the private key
sender_account = Account.from_key(PRIVATE_KEY)
PUBLIC_KEY = sender_account.address

# Connect to the Base network using the provided RPC URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Check network connection
if not web3.is_connected():
    raise ConnectionError("Connection failed to the Base network")

print(f"Connected to the Base network. Sender: {PUBLIC_KEY}")

# Convert the DEGEN token contract address to a checksum address
degen_token_address = Web3.to_checksum_address('0xd3c68968137317a57a9babeacc7707ec433548b4')

# DEGEN token ABI
token_abi = [
    {"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},
    {"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}
]

# Create the contract instance
degen_contract = web3.eth.contract(address=degen_token_address, abi=token_abi)

# Manually set gas price to 0.02 gwei for all transactions
fixed_gas_price = web3.to_wei('0.05', 'gwei')

# Fetch nonce initially
nonce = web3.eth.get_transaction_count(PUBLIC_KEY)

# Function to send DEGEN tokens to the recipient wallet
def send_degen_token(amount):
    global nonce  # Reuse the nonce for subsequent transactions
    try:
        # Build the transaction
        transaction = degen_contract.functions.transfer(RECIPIENT_WALLET, amount).build_transaction({
            'chainId': 8453,  # Base network chain ID
            'gas': 100000,    # Set an efficient gas limit
            'gasPrice': fixed_gas_price,  # Fixed gas price at 0.02 gwei
            'nonce': nonce
        })

        # Sign the transaction with the private key
        signed_txn = web3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

        # Send the signed transaction
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f"Transaction successful with hash: {web3.to_hex(tx_hash)}")

        # Increment nonce to avoid network call for fetching nonce again
        nonce += 1

    except Exception as e:
        print(f"Error sending transaction: {e}")

# Function to check the DEGEN balance of the wallet
def check_degen_balance():
    try:
        balance = degen_contract.functions.balanceOf(PUBLIC_KEY).call()
        print(f" Balance: {balance}")
        return balance
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return 0

# Main loop that continuously checks the balance and sends DEGEN tokens if detected
while True:
    degen_balance = check_degen_balance()
    if degen_balance > 0:
        print(f"DEGEN tokens detected: {degen_balance}")
        send_degen_token(degen_balance)  # Send all available tokens
        print(f"Sent {degen_balance} DEGEN tokens to {RECIPIENT_WALLET}")
    time.sleep(0.05)