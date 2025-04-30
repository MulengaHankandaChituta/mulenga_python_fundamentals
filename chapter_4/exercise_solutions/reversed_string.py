"""
Assume that the variable myString refers to a string. Write a code 
segment that uses a loop to print the characters of the string in 
reverse order
"""

# declarer variables

myString = "Rachael"
reversedString = ""

# loop through the string
for char in myString:
    reversedString = char + reversedString

print(reversedString)