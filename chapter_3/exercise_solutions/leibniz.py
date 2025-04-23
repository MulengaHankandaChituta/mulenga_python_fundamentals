"""The German mathetician Gottfried Leibniz developed the following method 
to approximate the value of pi: n/4 = 1 - 1/3 + 1/5 - 1/7 + ...
Write a program in the file leibniz.py that allows the user to specify
the number of iterations used in this approximation and displays the 
resulting value."""

iterations = int(input("Enter the number of iterations: "))

pi_over_4 = 0
for i in range(iterations):
    if i % 2 == 0:
        pi_over_4 += 1 / (2 * i + 1)
    else:
        pi_over_4 -= 1 / (2 * i + 1)

pi = pi_over_4 * 4
print("Aproximated value of π:", pi)
