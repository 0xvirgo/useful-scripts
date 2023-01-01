"""
This script will create a csv file from ERC721 token metadata in json files.
"""

import csv
import json

# TODO: Add path to directory that contains json files
json_files_directory = ""
# TODO: Add path to csv file
csv_file = ""
# TODO: Replace total number of tokens plus one
total_tokens_plus_one = 6777
# TODO: Replace token name
token_name = "Vales #"
# TODO: Replace headers based on token attributes
header = ['Token ID', 'Token Name', 'Background', 'Type', 'Eyes', 'Mouth', 'Clothes', 'Hair']

# Open our existing CSV file in append mode
# Create a file object for this file
with open(csv_file, 'a') as outfile:

    # Pass this file object to csv.writer() and get a writer object
    writer_object = csv.writer(outfile)

    # Append wallet address to csv file
    # Pass the wallet address as an argument into the writerow()
    writer_object.writerow(header)

    # Close the file object
    outfile.close()

# Write data from all json files
for x in range(1, total_tokens_plus_one):
    list = []

    # Set json file to be opened
    file_name = json_files_directory + str(x) + ".json"

    # Open json file
    a_file = open(file_name, "r")
    json_object = json.load(a_file)

    # Close json file
    a_file.close()

    # TODO: Replace token attributes
    background = json_object["attributes"][0]['value']
    type = json_object["attributes"][1]['value']
    eyes = json_object["attributes"][2]['value']
    mouth = json_object["attributes"][3]['value']
    clothes = json_object["attributes"][4]['value']
    hair = json_object["attributes"][5]['value']

    list.append(str(x))
    list.append(token_name + str(x))

    # TODO: Replace token attributes
    list.append(background)
    list.append(type)
    list.append(eyes)
    list.append(mouth)
    list.append(clothes)
    list.append(hair)

    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open(csv_file, 'a') as outfile:
        # Pass this file object to csv.writer() and get a writer object
        writer_object = csv.writer(outfile)
    
        # Append wallet address to csv file
        # Pass the wallet address as an argument into the writerow()
        writer_object.writerow(list)
    
        # Close the file object
        outfile.close()
