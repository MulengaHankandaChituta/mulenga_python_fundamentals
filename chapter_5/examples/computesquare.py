"""
File: computesquare
Illustrates the definition of a main function
"""

def main():
    """The main function for this script."""
    number = float(input("Enter a number: "))
    result = square(number)
    print("The square of", "is", result)

def square(x):
    return x * x

# teh entry point for program execution
if __name__ == "__main__":
    main()