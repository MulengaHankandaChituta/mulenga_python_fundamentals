"""An objects momentum is its mass multiplied by its velocity. Write a program in the file
momentum.py that accepts an object's mass (in kilograms) and velocity(in meters per second) 
as inputs and the outputs its momentum"""

# Ask the user for input

mass = int(input("Enter the mass: "))
velocity = int(input("Enter the velocity: "))

# calcultae the momentum

momentum = mass * velocity

# output the results

print("The momentum is ", momentum)

