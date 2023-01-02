# Secure Password Generator

import argparse
import random
import string

"""
Generates a random, secure password.

Parameters: 
--length [number] (Ex. --length 20)
--include-symbols (if added, will generate with symbols | if not added, default is false)

Returns:
- Generated password
"""

# Define generate function
def genPassword(length, include_symbols=False):
    # Create a list of possible characters to include
    characters = string.ascii_letters + string.digits
    if include_symbols:
        characters += string.punctuation
    # Choose random characters from list to create password
    password = "".join(random.choices(characters, k=length))
    return password

# create argument parser object
parser = argparse.ArgumentParser()

# Add command-line option for length
parser.add_argument("--length", type=int, help="Length of password to generate")
# Add command-line option for symbols
parser.add_argument("--include-symbols", action="store_true", help="Include symbols in the password")
# parse the command-line arguments
args = parser.parse_args()

# Generate a password with characters and symbols
password = genPassword(args.length, include_symbols=args.include_symbols)
print(password)
