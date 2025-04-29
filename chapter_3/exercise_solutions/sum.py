"""
Write a program in the file sum.py that receives a series of numbers
from the user and allows the user to press the enter key to indicate
that he or she is finished providing inputs. After the user pressses
the enter key, the program should print the sum of the numbers and their
average.
"""
# Ask the user for inputs

numbers = []
print("Enter numbers one by one. Press Enter without typing anything to finish")

while True:
    num = input("Enter a number: ")
    if num == "":
        break
    numbers.append(float(num))
if len(numbers) > 0:
    total = 0
    for n in numbers:
        total += n
    average = total / len(numbers)
    print("Sum of numbers:", total)
    print("Average of numbers:", average)
