"""Write a program in the file minutes.py that takes as input a number of years
and calculates and prints the number of minutes in that period of time."""


# declare a constant variable for minutes in a year

min_in_year = 525600

# ask user to input the number of years

years = int(input("Enter the number of years: "))

# calculate the number of minutes in a year

minutes_in_years = years * min_in_year

# display the  output

print("There are ", minutes_in_years, "minutes in", years, "years")