"""Write a program in the file klickstonauts.py that takes as input a number
of kilometers and prints  the corresponding number of nautical miles. Use the
following approximations.
1. A kilometer represents 1/10,000 of the distance between the Norht Pole and the equator.
2. There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
3. A nautical mile is 1 minute of an arc."""

# The code will use the constant for one nautical mile being equal 
# to the number of kilometers in a constant variable

# declare constant variable for one nautical mile

one_nautical_mile = 1.852 # one nautical mile is 1.852 kilometers

# ask user for input in kilometers

kilometers = float(input("Enter the number of kilometers: "))

# make the calculation

nautical_miles = kilometers / one_nautical_mile

# Display the result

print("The number of nautical miles in ", kilometers, "kilometers is ", nautical_miles, "nautical miles")



