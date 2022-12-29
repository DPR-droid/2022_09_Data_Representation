# Data Representation
# Lecturer: Andrew Beatty
# Author: David Ryan
# Student ID: G00398318

import os

# Request input from the user
virustotal_api_key = input("Enter your VirusTotal API key: ")

# Create the config dictionary with the user's input
config = {
    "virustotal": virustotal_api_key
}

# Create the config.py file and write the config dictionary to it
with open("config_test.py", "w") as config_file:
    config_file.write("config = " + str(config))

print("config.py file created successfully!")