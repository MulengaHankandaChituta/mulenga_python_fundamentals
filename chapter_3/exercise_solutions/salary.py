"""
Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years teaching experience. For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year.
For each year of experience after this first year, up to 10 years, the teacher
receives 2% increase over the preceeding value. Write a program in the file salary.py
that displays a salary schedule, in tabular format, for teachers in a school 
district. The inputs are the starting salary, the percentage increase, and
the number of years in the schedule. each row in the schedule should contain
the year number and the salary for that year.
"""

# ask the user for inputs

starting_salary = float(input("Enter the starting salary: "))
percentage = float(input("Enter the percentage increase: "))
number_of_years = int(input("Enter the number of years: "))

# Convert the percentage to decimal

percentage_increase = percentage /  100

# Formatted table displayed here

print("%4s%18s%10s%16s" % ("Year", "Salary", "", ""))
print("-" * 50)

# Salary Ininialized with starting salary

salary = starting_salary

# Loop  through the years and display the salary for each year

for year in range(1, number_of_years + 1):

    # Display results in tabular format
    print("%4d%18.2f%10s%16s" % (year, salary, "", ""))

    # Update the salary for the next year

    salary = salary * (1 + percentage_increase)