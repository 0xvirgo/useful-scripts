"""
This script transfers nfts from a single wallet to a list of wallet addresses. 
A single transaction transfers 100 nfts.
"""
from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
import datetime
import time
from time import strftime
from time import gmtime
import csv
from math import floor

# Get start time of script execution
start_time = time.time()

# TODO: Replace lowest token id in collection
lowest_token_id_in_collection = 1
# TODO: Replace highest token id in collection
highest_token_id_in_collection = 6776
# TODO: Replace highest token id plus one in collection
highest_token_id_plus_one_in_collection = 6777

# TODO: Add mainnet connector
mainnet_connector = Connect("")
# TODO: Add mainnet wallet address
mainnet_wallet_address = ''
# TODO: Add mainnet contract address
mainnet_contract_address = ''
# TODO: Add mainnet contract abi
mainnet_contract_abi = Contract.fromFile("")
# TODO: Add mainnet wallet mnemonic words
mainnet_wallet = Wallet.fromMnemonic(words=[])
# TODO: Add path to file that contains list of wallets
wallets_list_file = ''
with open(wallets_list_file, newline='') as csvfile:
    mainnet_list_wallet_addresses = list(csv.reader(csvfile))

# TODO: Add directory to store log files
directory = ""

# Current date and time including seconds
current_date_time = datetime.datetime.now().strftime("%d-%d-%Y-%H-%M-%S")

# File to store logs about bulk transfer
log_file = directory + "bulk-transfer-log-" + current_date_time + ".txt"

print("Current date time: " + current_date_time)
print("Log File: " + log_file)

# Open log file in writing mode
file_object = open(log_file, "w+")

# Write current date time in log file
file_object.write("Current date time: %s\r\n\n" % (current_date_time))

# Total tokens divide by 100 functions per transaction
batch_transfer_loop = floor(highest_token_id_in_collection / 100)
print(batch_transfer_loop)

current_token_id = 1

for x in range(1, batch_transfer_loop):
    list = []

    # Transfer 100 NFTs in a single transaction
    for y in range(1, 101):
        print(y)
        print("current_token_id: %d" %(current_token_id))

        # Get recipient address
        mainnet_recipient_address = str(mainnet_list_wallet_addresses[current_token_id-1])[1:-1][1:-1]
        print(mainnet_recipient_address)

        list.append(mainnet_connector.clause(
            mainnet_contract_abi, 
            "safeTransferFrom", 
            [mainnet_wallet_address, mainnet_recipient_address, current_token_id], 
            mainnet_contract_address))

        current_token_id = current_token_id + 1

    print("x: %d\n\n" %(x))
    
    # Print transferring token id to destination address log to terminal
    print("Bulk transferring token id %d to %d\r\n" % (current_token_id-100, current_token_id-1))

    # Write bulk transferring token id to destination address in log file
    file_object.write("Bulk transferring token id %d to %d\r\n" % (current_token_id-100, current_token_id-1))

    # Execute the transactions
    safe_transfer_from = mainnet_connector.transact_multi(mainnet_wallet, clauses=list)
    print(safe_transfer_from)

    # Extract transaction id of executed safeTransferFrom() function
    safe_transfer_from_transaction_id = safe_transfer_from['id']

    # Print transaction id to destination address log to terminal
    print("Transaction id: %s\r\n\n" % (safe_transfer_from_transaction_id))

    # Write to transferring token id to destination address in log file
    file_object.write("Transaction id: %s\r\n\n" % (safe_transfer_from_transaction_id))

    current_token_id = current_token_id + 100

# Get end time of script execution
end_time = time.time()

# Calculate execution time
execution_time = strftime("%H:%M:%S",gmtime(int('{:.0f}'.format(float(str((end_time-start_time)))))))

# Print script execution time in seconds
print("\nExecution Time: " + execution_time)

# Write to transferring token id to destination address in log file
file_object.write("Execution Time: " + execution_time)

# Close log file
file_object.close()
