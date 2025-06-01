"""
Modify the scripts of programming exercises 1 and 2
to encrypt and decrypt entire files of text.
"""

# Import libraries
import string

# All printable characters
printable_chars = string.printable
n = len(printable_chars)

def caeser_decrypt(text, distance):
    plain = ""
    for ch in text:
        if ch in printable_chars:
            index = printable_chars.index(ch)
            plainIndex = (index - distance) % n
            plain += printable_chars[plainIndex]
        else:
            plain += ch
    return plain

def main():
    input_file = input("Enter the input filename (encrypted): ")
    output_file = input("Enter the output filename (decrypted): ")
    distance = int(input("Enter the distance value: "))

    try:
        with open(input_file, 'r') as f:
            content = f.read()
        decrypted = caeser_decrypt(content, distance)
        with open(output_file, 'w') as f:
            f.write(decrypted)
        print("Decryption complete. Output saved to", output_file)
    except FileNotFoundError:
        print("Error: File not found.")

if __name__ == "__main__":
    main()
