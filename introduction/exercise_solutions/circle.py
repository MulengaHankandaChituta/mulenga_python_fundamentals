"""Write and test a program in a file called circle.py that computes the area of a circle.
This program should request a number representing a radius as input from the user.It should
use the formula 3.14 * radius ** 2 to compute the area and then output this result suitably
labeled"""

radius = float(input("Enter the radius: "))
pi = 3.14
area = pi * radius ** 2
print("The area of the circle is ", area,  " square units")