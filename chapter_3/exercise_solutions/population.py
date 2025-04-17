"""A local biologist needs a program to predict population growth. The inputs would be the 
Initial number of organisms, the rate of growth(a real number greater than 0), the number
of hours it takes to achieve this rate, and a number of hours during which the population
grows. For example, one might start with a population of 500 organisms, a growth period
to achieve this rate of 6 hours. Assuming that none of the organisms die, this would imply
that this population would double in size every 6 hours. Thus, after allowing 6 hours of
growth, we would have 1000 organisms, and after 12 hours, we would have 2000 organisms.
Write a program in the file population.py that takes these inputs and displays a prediction
of the total population."""

# declare a constant

rate_of_growth = 1.0

# Ask the user for input

initial_organisms = float(input("Enter the number of organisms: "))

# ask user to enter the growth rate in hours
hours_per_growth_period = float(input("Enter hours per growth period: "))

# Ask user to enter the number of hours of growth
hours_of_growth = float(input("Enter number of hours of growth: "))

while True:
    population = initial_organisms * (1 + rate_of_growth) * (hours_of_growth / hours_per_growth_period)
    print("The population is ", population, "organisms")
    break



