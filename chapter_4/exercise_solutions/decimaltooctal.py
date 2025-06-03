
"""
Octal numbers have a base of eight and the digits 0-7.
Write the scripts octaltodecimal.py and decimaltooctal.py,
which convert numbers between the octal and decimal representations
of integers. These scripts use algorithms that are similar to those
of the binaryTodecimal and decimalToBinary scripts developed in section
4-3.
"""

# ask the user for input
decimal = int(input("Enter a decimal integer: "))

def decimal_to_octal(decimal_num):
    """This function converts a decimal number to octal"""
    if decimal_num == 0:
        return "0"
    
    octal = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal = str(remainder) + octal
        decimal_num = decimal_num // 8
    return octal

if decimal < 0:
    print("Only non-negative numbers are allowed.")
else:
    octal_output = decimal_to_octal(decimal)
    print("The octal representation is:", octal_output)