"""Light travels at 3 * 10**8 meters per second. A light-year is the distance a light beam
travels in one year. Write a program int the file lightyear.py that expects a number of years
as input and calculates and displays the value of the distance traveled  in meters"""


# declare constant variables needed by program

speed_of_light = 299792458
seconds_in_one_year = 31536000

# ask the user for some input

years = float(input("Enter the number of years: "))

# calculate the number of light years

light_years = (speed_of_light * seconds_in_one_year) * years

# Output the result

print("The number of lightyears in", years, "years is", light_years, "miles")



