"""A cuboid is a solid figure bounded by six rectangular faces. Its dimensions
are its height, width, and depth. Write a program in a file named cuboid.py that
computes and prints the volume of a cuboid, given its height, width, and depth as 
inputs. The volume is just the product of these three inputs. The output be labeled
as 'cubic units.'"""

length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
volume = length * width * height

print("The volume of the cuboid is ", volume, "cubic units")