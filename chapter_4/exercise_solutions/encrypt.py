"""
Write a script in the file encrypt.py that inputs a line of plaintext
and a distance value and outputs and encrypted text using a Caeser cipher.
The script should work for any printable characters.
"""
# import necessary libraries
import string

# Define all printable characters
printable_chars = string.printable
n = len(printable_chars)

# get input from user

plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))

code = ""
for ch in plainText:
    if ch in printable_chars:
        index = printable_chars.index(ch)
        cipherIndex = (index + distance) % n
        code += printable_chars[cipherIndex]
    else:
        code += ch # leave non-printable characters unchanged (just in case)

print("Encrypted message:", code)
