"""Write a program in the file sphere.py that takes the radius of a sphere(a floating point number)
as input and then outputs the sphere's diameter, circumference, surface area, and volume"""


# declare a constant variable
pi = 3.142

# ask the user to input the radius
radius = float(input("Enter the radius of the sphere: "))

# Calculate the sphere's diameter, circumference, surface area, and volume
diameter = 2 * radius
surface_area = 4 * pi * radius ** 2
volume = (4/3) * pi * radius ** 3
circumference = 2 * pi * radius

# Output the results
print("The diameter is ", diameter)
print("The surface area is ", surface_area)
print("The volume is ", volume)
print("The circumference is ", circumference)

