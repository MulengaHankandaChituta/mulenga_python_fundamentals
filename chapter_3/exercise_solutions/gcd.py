"""
The greatest common divisor of two positive integers, A and B, is
the largest number that can be evenly divided into both of them.
Euclid's algorithm can be used to find the greatest common divisor
(GCD) of two positive integers. You can implement this algorithm
in the following manner.
a. Compute the remainder of dividing the larger number by the smaller number.
b. Replace the larger number with the smaller number and the smaller number with the remainder
c. Repeat this process until the smaller number is zero.
d. The larger number at this point is the GCD of A and B. Write a program in the file gcd.py
   that lets the user enter two integers and then prints each step in the process of using
   the Euclidean algorithm to fin their GCD.
"""

# ask user for input
a = int(input("Enter the first positive integer (A): "))
b = int(input("Enter the second positive integer (B): "))

# Make sure the a is the larger number

if a < b:
    a, b = b, a

print("Starting Euclidean Algorithm:")

# Looping until the smaller number becomes zero

while b != 0:
    remainder = a % b
    print(f"{a} / {b} = {a // b} remainder {remainder}")
    a, b = b, remainder

print(f"\nThe GCD is {a}.")