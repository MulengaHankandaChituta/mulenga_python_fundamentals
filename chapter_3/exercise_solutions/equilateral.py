"""
Write a program in the file equilateral.py that accepts the lengths
of three sides of a triangle as inputs. The program output should
indicate whether or not the triangle is an equilateral tringle.
"""

# ask user for inputs

side_1 = int(input("Enter the length of side one: "))

side_2 = int(input("Enter the length of side two: "))

side_3 = int(input("Enter the length of side three: "))

# check if all sides are equal

if side_1 == side_2 == side_3:
    print("The triangle is equilateral")
else:
    print("Error: the trinagle is not equilateral, all sides must be equal.")