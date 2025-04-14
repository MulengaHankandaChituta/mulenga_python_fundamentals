"""
Write a program in the file right.py that accepts the lengths 
of three sides of a tringle as inputs. The program output
should indicate whether or not the triangle is a right triangle.
Recall from the pythagorean theorem that in a right triangle,the
square of one side equals the sum of the squares of the other
two sides
"""
# ask the user for inputs

side_1 = int(input("Enter the length of side one: "))
side_2 = int(input("Enter the length of side two: "))
side_3 = int(input("Enter the length of side three: "))

# calculate the pythagorean theorem

if side_1 ** 2 + side_2 ** 2 == side_3:
    print("The tringle is a right triangle")
else:
    print("Error the triangle is not a right triangle")