"""An employee's total  weekly pay equals the hourly wage multiplied by the total number
of regular hours plus any overtime pay. Overtime pay equals the total overtime hours
multiplied by 1.5 times the hourly wage. Write a program in the file employeepay.py
that takes as inputs the hourly wage, total regular hours, and total overtime hours
and displays an employees total weekly wage"""

# Declare the constant variable for hourly pay 

hourly_wage = 14


# Ask user to input hours worked and overtime worked

hours_worked = int(input("Enter the number of hours worked: "))
overtime_worked = int(input("Enter overtime hours worked: "))

# Calculate normal hours pay, overtime rate, and overtime pay

regular_pay = hours_worked * hourly_wage
overtime_rate = hourly_wage * 1.5
overtime_pay = overtime_worked * overtime_rate

# Calculate total weekly wage

total_weekly_wage = regular_pay + overtime_pay

# Display results

print("The total weekly wage is ", total_weekly_wage, "kwacha")



