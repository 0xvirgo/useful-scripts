from thor_devkit.cry import mnemonic
from thor_devkit import cry
from thor_devkit.cry import hdnode
import csv

# TODO: Replace total wallet addresses to generate plus one
total_wallet_addresses_to_generate = 6777

# TODO: Add path to csv file that will store wallet addresses
file = ''

wallet_addresses_list = []

# Generate wallets
for x in range(1, total_wallet_addresses_to_generate):
    flag = False

    while flag == False:
        words = mnemonic.generate()
        print(words)

        flag = mnemonic.validate(words)
        print(flag)

    converted_word_list = ' '.join(words)
    print(converted_word_list)

    # Construct an HD node from words
    words_for_hd_node = converted_word_list.split(' ')

    hd_node = cry.HDNode.from_mnemonic(
        words,
        init_path=hdnode.VET_EXTERNAL_PATH
    )

    # Access the HD node's properties.
    priv = hd_node.private_key()
    pub = hd_node.public_key()
    addr = hd_node.address()
    cc = hd_node.chain_code()

    _address_bytes = cry.public_key_to_address(pub)
    address = '0x' + _address_bytes.hex()
    print(address)

    wallet_addresses_list.append(address)

print(wallet_addresses_list)
print("Number of wallet addresses: " + str(len(wallet_addresses_list)))

with open(file, 'w') as f:
    writer = csv.writer(f)
    for val in wallet_addresses_list:
        writer.writerow([val])
