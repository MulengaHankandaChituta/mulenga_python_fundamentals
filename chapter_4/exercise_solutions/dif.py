"""
Write a script named dif.py. This script should prompt the user
for names of two text files and compare the contents of the two
files to see if they are the same.If they are, the script should simply
output "Yes".If they are not, the script should output "No", followed by 
the first lines of each file that differ from each other.The input
loop should read and compare lines from each file.The loop should break
as soon as a pair of different lines is found.
"""

def compare_files():
    file1_name = input("Enter the name of the first file: ")
    file2_name = input("Enter the name of the second file: ")

    try:
        with open(file1_name, 'r') as file1, open(file2_name, 'r') as file2:
            line_num = 1
            while True:
                line1 = file1.readline()
                line2 = file2.readline()

                # Both files reach end of file at the same time
                if line1 == '' and line2 == '':
                    print("Yes")
                    return
                
                # If lines differ or one file ends earlier
                if line1 != line2:
                    print("No")
                    print(f"First difference at line {line_num}:")
                    print(f"{file1_name}: {line1.strip()}")
                    print(f"{file2_name}: {line2.strip()}")
                    return
                line_num += 1
    
    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Run the program
if __name__ == "__main__":
    compare_files()