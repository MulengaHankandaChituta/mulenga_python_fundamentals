"""
Write a script named copyfile.py. This script should prompt the user
for the names of two text files. The contents of the first file should
be input and written to the second file.
"""
def copy_file():
    source = input("Enter the name of the source file: ")
    destination = input("Enter the name of the destination file: ")

    try:
        with open(source, 'r') as src_file:
            content = src_file.read()
        
        with open(destination, 'w') as dest_file:
            dest_file.write(content)

        print(f"Contents copied from '{source}' to '{destination}' successfully.")

    except FileNotFoundError:
        print(f"Error: Thefile '{source}' does not exist.")
    except IOError as e:
        print(f"An I/O error occured: {e}")

# Run the program
if __name__ == "__main__":
    copy_file()