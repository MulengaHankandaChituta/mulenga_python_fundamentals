"""A standard science experiment is to drop a ball  and see how high it bounces.
Once the 'bounciness' of the ball of the ball has been determined, the ratio gives
a bounciness index. For example, if a ball dropped from a height of 10 feet bounces
6 feet high, the index is 0.6, and the total distance traveled by the ball is 16 feet 
after one bounce. If the ball were to continue bouncing, after two bounces would be 
10 ft + 6 ft + 6 ft + 3.6 ft = 25.6 ft. Note that the distance traveled for each
successive bounce is the distance to the floor plus 0.6 of that distance as the
ball comes back up. Write a program in the file bouncy.py that lets the user enter
the initial height from which the ball is dropped and the number of times the ball
is allowed to continue bouncing. Output should be the total distance traveled by the
ball."""

# Declare a constant variable

index = 0.6

# ask the user for input

initial_height = float(input("Enter the initial height: "))

bounces_allowed = float(input("Enter the bounces allowed: "))

while True:
    distance_traveled = initial_height + 2 * initial_height * index * ((1 - index ** bounces_allowed) / (1 - index))
    print("The distance traveled is %0.1f "  % distance_traveled,"feet")
    break




