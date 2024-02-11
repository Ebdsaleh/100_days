# main.py
# Day 08 Project - Caesar Cipher
import art

"""
This program takes user input and encodes or decodes the input based on the
shift amount.
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:
            position = alphabet.index(char)
            new_pos = position + shift
            end_text += alphabet[new_pos]
        else:
            end_text += char
        print(f"The {direction}d text is {end_text}")


def will_continue():
    again = input("Run again? 'yes' or 'no'").lower()
    if again[0] == 'y':
        return True
    elif again[0] == 'n':
        return False


def run_cipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(text, shift, direction)
    if will_continue():
        return
    else:
        exit()


def main():
    logo = art.logo
    print(f"{logo}")
    while True:
        run_cipher()


if __name__ == '__main__':
    main()
