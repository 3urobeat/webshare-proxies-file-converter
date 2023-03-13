#!/usr/bin/python3

'''
File: proxyConverter.py
Project: webshare-proxies-file-converter
Created Date: 13.03.2023 22:18:12
Author: 3urobeat

Last Modified: 13.03.2023 23:04:27
Modified By: 3urobeat

Copyright (c) 2023 3urobeat <https://github.com/HerrEurobeat>

Licensed under the MIT license: https://opensource.org/licenses/MIT
Permission is granted to use, copy, modify, and redistribute the work.
Full license information available in the project LICENSE file.
'''


# Quick and dirty lil py script to convert the https://webshare.io proxy file to something https://github.com/HerrEurobeat/steam-comment-service-bot understands
# File must be in the same directory as this script and named "input.txt"
# Script will create and write to a file called "proxies.txt" so that you can instantly copy it to the folder of your steam-comment-service-bot installation.


# Imports
import sys
import os.path


# Print welcome msg
print("webshare-proxies-file-converter v1.0 by 3urobeat\n")


# Check if input file exists and abort if it doesn't
print("Checking if file exists...")

if not os.path.exists("input.txt"):
    print("Error: Input file does not exist! Please make sure it is called 'input.txt', is located in the same folder as this script and try again!")
    sys.exit()


# Open file
print("Opening file...")

inputFile = open("input.txt", "r") # Open input.txt with read perms


# Create proxies.txt file
print("Creating empty proxies.txt file...")

outputFile = open("proxies.txt", "w") # Create and open output file

outputFile.write("") # Clear any content


# Convert and append to new file
print("Converting and appending to new file...")

# Write to a new file
print("Creating and writing to a new file...")


# End
print("Done! Exiting...")