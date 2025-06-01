"""
Write a script in the file decrypt.py tha inputs
a line of encrypted text and a distance value
and outputs plaintext using a Caeser cipher. The
script should work for any printable characters.
"""

# import libraries
import string

# Define all printable characters
printable_chars = string.printable # Includes digits, letters, punctuation, whitespace
n = len(printable_chars)

# As user for input
cipherText = input("Enter the encrypted message: ")
distance  = int(input("Enter the distance value: "))

# Perform the decryption
plainText = ""
for ch in cipherText:
    if ch in printable_chars:
        index = printable_chars.index(ch)
        plainIndex = (index - distance) % n
        plainText += printable_chars[plainIndex]
    else:
        plainText += ch # Leave unknown characters unchanged

print("Decrypted message:", plainText)