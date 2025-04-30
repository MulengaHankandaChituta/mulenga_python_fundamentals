"""
In the game of Lucky Sevens, the player rolls a pair of dice. If the dots
add up to seven the player wins K4; otherwise, the player loses K1. Suppose
that, to entice the gullible, a casino tells players that there are lots of ways
to  win: (1,6), (2,5), and so on. A little mathematical analysis reveals that there
no enough ways to win to make the game worthwhile; however, because many people's
eyes glaze over at the first mention of mathematics, your challenge is to write
 a program in the file sevens.py that demonstrates the futility of playing the game
 until the pot is empty. At that point, the program should print the number of rolls
 it took to break the player, as well as maximum amount of money in the pot.
"""

import random

# show a welcoming message

print("Welcome to the Lucky Sevens Game!")

# Get initial pot amount

pot = int(input("Enter the amount of money to start with: K"))

# Initialize counters

initial_pot = pot
rolls = 0
max_pot = pot
max_roll = 0

# Game loop

while pot > 0:
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    total = die1 + die2

    # Update pot based on result
    if total == 7:
        pot += 4
    else:
        pot -= 1

        # Update counters
        rolls += 1

        # Track max pot

        if pot > max_pot:
            max_pot = pot
            max_roll = rolls

# Display results

print("\nYou are broke after", rolls, "rolls.")
print("You should have quit after", max_roll, "rolls when you had K%d." % max_pot)
