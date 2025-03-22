"""Open an IDLE window and enter the program from figure 1-7 that computes the area of a rectangle.
Save the program to a file named rectangle.py and load it into the shell by pressing the F5 key
and correct any errors that occur, Test the program with different inputs by running it atleast three times"""

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))
perimeter = (length + breadth) * 2
print("The perimeter is", perimeter, "centimetres")