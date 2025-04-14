"""
The log of a given number N is given by M in the equation
N = 2 ** M Using integer arithmetic, the value of M is
approximately equal to the number of times N can be
evenly divided by 2 until it becomes 0. Write a loop that 
computes this aproximation of the log of a given number N. 
You can check your code by importing the the math.log funtion
and evaluating the expression round(math.log(N, 2)) (note
that the math.log function returns floating-point value).
"""
import math

number = 8
exponent = 2

while number == 8:
    print(f"The number of times", number, "can be evenly divided by"
          , exponent,"is",(round(math.log(number, exponent))),"times")
    number += 1

