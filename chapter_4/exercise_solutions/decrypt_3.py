"""
Write a script in the file decrypt_3.py that decrypts
a message coded by the method used in Programming
exercise 6 called encrypt_3.py
"""

def binary_to_decimal(bitString):
    """Manually converts a binary string to decimal integer."""
    decimal = 0
    power = len(bitString) - 1
    for bit in bitString:
        decimal += int(bit) * (2 ** power)
        power -= 1
    return decimal

def shift_right(bits):
    """Shifts binary digits one bit to the right by moving last bit to front."""
    if not bits:
        return bits
    return bits[-1] + bits[:-1]

def decrypt(encrypted_text):
    """Decrypts a string by reversing the encrypt_3.py process."""
    decrypted = []
    bit_strings = encrypted_text.strip().split()

    for bit_str in bit_strings:
        shifted_back = shift_right(bit_str)
        decimal_val = binary_to_decimal(shifted_back)
        ascii_val = decimal_val - 1
        decrypted.append(chr(ascii_val))
    return ''.join(decrypted)

# Ask the user for input and run the decryption
if __name__ == "__main__":
    user_input = input("Enter encrypted binary string: ")
    result = decrypt(user_input)
    print("Decrypted text:")
    print(result)