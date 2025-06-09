"""
Use the strategy of the decimal to binary conversion
and the bit shift left operation defined in Programming
exercise 5 to code a new encryption algorithm in the file
encrypt_3.py. The algorithm should add 1 to each character's
numeric ASCII value, convert it to a bit string, and shift
the bits of this string one place to the left. A single-space
character in the encrypted string seperates the resulting bit
"""

def decimal_to_binary(decimal):
    """Manually converts a decimal to an 8-bit binary string."""
    if decimal == 0:
        return '00000000'
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
    return bitString.zfill(8) # This ensures 8-bit format

def shift_left(bits):
    """Shifts binary digits one bit to the left and appends a 0 at the end."""
    if not bits:
        return bits
    return bits[1:] + '0'

def encrypt(text):
    """Encrypts a string by applying ASCII+1, binary conversion, and left bit shift."""
    encrypted = []
    for char in text:
        ascii_val = ord(char) + 1
        binary = decimal_to_binary(ascii_val)
        shifted = shift_left(binary)
        encrypted.append(shifted)
    return ' '.join(encrypted)

# Ask the user for input and run encryption
if __name__ == "__main__":
    user_input = input("Enter text to encrypt: ")
    result = encrypt(user_input)
    print("Encrypted binary string:")
    print(result)