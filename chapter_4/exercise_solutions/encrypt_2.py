"""
Modify the scripts of programming Exercises
1 and 2 to encrypt and decrypt entire files
of text.
"""
# Import libraries
import string

# All printable characters
printable_chars = string.printable
n = len(printable_chars)

def caeser_encrypt(text, distance):
    code = ""
    for ch in text:
        if ch in printable_chars:
            index = printable_chars.index(ch)
            cipherIndex = (index + distance) % n
            code += printable_chars[cipherIndex]
        else:
            code += ch
    return code

def main():
    input_file = input("Enter the input filename (plaintext): ")
    output_file = input("Enter the output filename (encrypted): ")
    distance = int(input("Enter the distance value: "))

    try:
        with open(input_file, 'r') as f:
            content = f.read()
        encrypted = caeser_encrypt(content, distance)
        with open(output_file, 'w') as f:
            f.write(encrypted)
        print("Encryption complete. Output saved to", output_file)
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()