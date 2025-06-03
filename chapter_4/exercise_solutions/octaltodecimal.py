"""
Octal numbers have a base of eight and the digits 0-7.
Write the scripts octaltodecimal.py and decimaltooctal.py,
which convert numbers between the octal and decimal representations
of integers. These scripts use algorithms that are similar to those
of the binaryTodecimal and decimalToBinary scripts developed in section
4-3.
"""

octal = input("Enter an octal number (digits 0-7): ")

def octal_to_decimal(octal):
    """This function converts octal to decimal"""
    decimal = 0
    power = 0
    for digit in reversed(octal):
        if digit  not in '01234567':
            raise ValueError("Invalid octal digit: " + digit)
        decimal += int(digit) + (8 ** power)
        power += 1
    return decimal

try:
    decimal_output = octal_to_decimal(octal)
    print("The decimal representation is:", decimal_output)
except ValueError as e:
    print("Error:", e)
