"""
The credit plan at TidBit Computer Store specifies a 10% down
payment and an annual interest rate of 12%. Monthly payments
are 5% of the listed purchase price, minus the down payment. 
Write a program in the file tidbit.py that takes the purchase
price as input. The program should display a table, with
appropriate headers, of a payment schedule for the lifetime
of the loan. Each row of the table should contain the following
items:

1. The month number(beginning with 1)
2. The current total balance owed
3. The interest owed for that month
4. The amount of principal owed for that month
5. The payment for that month
6. The balance remaining after payment

The amount of interest for a month is equal to balance * rate / 12.
The amount of principal for a month is equal to the monthly 
payments minus the interest owed.
"""

# Ask user to input a purchase price

purchase_price = float(input("Enter the purchase price: "))

# Make necessary calculations

down_payment = 0.10 * purchase_price
annual_interest_rate = 0.12
monthly_payment = 0.05 * purchase_price
balance = purchase_price - down_payment
month = 1

# print the table header

print("\n%-6s %-12s %-12s %-12s %-12s %-12s" % 
      ("Month", "Balance", "Interest", "Principal", "Payment", "New Balance"))

# Loop through to calculate and display payment schedule

while balance > 0:
    interest = balance * annual_interest_rate / 12

    if monthly_payment > balance + interest:
        monthly_payment = balance + interest # last payment should be adjusted

    principal = monthly_payment - interest
    new_balance = balance - principal

    # print the final  output
    print("%-6d K%-11.2f K%-11.2f K%-11.2f K%-11.2f K%-11.2f" % 
          (month, balance, interest, principal, monthly_payment,  new_balance))
    
    balance = new_balance
    month += 1
