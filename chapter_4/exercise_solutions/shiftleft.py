"""
A bit shift is a procedure, whereby the bits in a string
are moved to the left or to the right. For example,
we can shift the bits in the string 1011 two places
to the left to produce the string 1110. Note that the
leftmost two bits are wrapped around the right side of 
the string in this operation. Define two scripts, shiftleft.py
and shiftright.py, that expect a bit string as input. The script
shiftleft shifts the bits in its input one place to the rightmost
position. The script shiftRight performs the inverse operation.
Each script prints the resulting string. 
"""

# ask the user for input
bit_string = input("Enter a number (e.g., 1011): ")

def shift_left(bits):
    """This function shifts binary digits one bit to the left."""
    if not bits:
        return bits
    return bits[1:] + bits[0]

# validate input
if all(bit in '01' for bit in bit_string):
    result = shift_left(bit_string)
    print("Shifted left:", result)
else:
    print("Error: Input must be a string of bits (0s and 1s only).")