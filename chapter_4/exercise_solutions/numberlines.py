"""
Write a script named numberlines.py. This script creates
a program listing from a source program. This script
should prompt the user for names of two files. The input
filename could be the name of the script itself, but be
careful to use a different output filename! The script copies
the lines of text from the input file to the output file,
numbering each line as it goes. The line numbers should be
right-justified in four columns, so that the format of a line
in the output file lokks like this example:
1> This is the first line of text.
"""

def number_lines():
    input_filename = input("Enter the name of the input file: ")
    output_filename = input("Enter the name of the output file: ")

    if input_filename == output_filename:
        print("Error: Input and output filenames must be different.")
        return
    
    try:
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            line_number = 1
            for line in infile:
                # Strip existing newline to add clean line ending later
                formatted_line = f"{str(line_number).rjust(4)}> {line}"
                outfile.write(formatted_line)
                line_number += 1

        print(f"Lines from '{input_filename}' were numbered and saved to '{output_filename}'.")
    except FileNotFoundError:
        print("Error: The file '{input_filename}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Run the program
if __name__== "__main__":
    number_lines()