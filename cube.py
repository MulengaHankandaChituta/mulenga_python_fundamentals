"""You can calculate the area of a cube if you know the length of an edge.
Write a program in the file cube.py that takes length of an edge(an integer) as input
and prints the cube's surface area output."""

"""
1.Program should calculate the surface area of a cube.
2.It will do so by first asking the user to input a value.
3.It will take the value of the one side, and using the formula.
to calculate area of a cube will calculate the total surface area.
4.The results will be displayed after calculation has been performed.
"""

# Enter the value of a side
side = int(input("Enter a side: "))

# Calculate the surface area of the cube
area = 6 * side ** 2

# Display the result

print("The total surface area of the cube is ", area, "square units")
