"""Five Star Retro Video rents DVDs to the same connoisseurs who like to buy vinyl records.
The store rents new videos for $3.00 a night, and oldies for $2.00 a night. Write a program
in the file fivestar.py that the clerks at Five Star Retro Video can use to calculate the total
charge for a customer's video rentals. The program should prompt the user for the number of each
type of Video and output the total cost."""

"""
1. The program should be able to accept input from a user
2. The input should be number of videos rented both old and new
3. After accepting input it should calculate the prices 
4. Of both new and old videos rented by number rented
5. It should then out put the total price for all videos rented
"""


# Declare necessary variables
new_price = 3
old_price = 2


# Ask user to input the number of videos rented both old and new
new = int(input("Enter the number of new videos: "))
old = int(input("Enter the number of old videos: "))

# calculate total for each type of video and total of all videos combined
total_new_video = new * new_price
total_old_video = old * old_price
total_all_videos = total_new_video + total_old_video

# Output the total price of videos rented
print("The total cost of videos rented is ", "$" + str(total_all_videos))

