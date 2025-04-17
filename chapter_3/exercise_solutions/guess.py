"""
Modify the guessing-game program of Section 3.5 in the file guess.py so 
that the user thinks of a  number that the computer must guess. The computer
must make no  more than the minimum number of guesses, aand it must prevent
the user from cheating by entering misleading hints.(Hint:Use the math.log function to
compute the minimum number of guesses needed after the lower and upper bounds are entered)
"""
import math

print("Think of a number, and I will try to guess it!")
lower = int(input("Enter the smaller number: "))
upper = int(input("Enter the larger number: "))

max_guesses = math.ceil(math.log2(upper - lower + 1))
print(f"I will guess your number in at most {max_guesses} tries.")

count = 0
while lower <= upper:
    guess = (lower + upper) // 2
    count += 1
    print(f"My guess is {guess}.")
    feedback = input("Is it too small (s), too large (l), or correct (c)? ").strip().lower()

    if feedback == 'c':
        print(f"I got it in {count} tries!")
        break
    elif feedback == 's':
        lower = guess + 1
    elif feedback == 'l':
        upper = guess - 1
    else:
        print("Invalid input. Please enter 's', 'l', or 'c'.")

    if count > max_guesses:
        print("Hmm... I think you're cheating! 😅")
        break
else:
    print("Your responses are inconsistent. Are you sure you're not cheating?")
