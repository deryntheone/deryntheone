# This was done as part of my Cybersecurity course for the Girls Who Code (GWC) Pathways program for Summer 2026.

import string

# Variables

initialPosition = 0
shiftedPosition = 0

shiftedMessage = ""

upper = string.ascii_uppercase
lower = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

characters = upper + lower + numbers + symbols

# Functions

def cipher():
    global shiftedPosition 
    if mode.lower() == "encrypt":
        shiftedPosition = initialPosition + key
    elif mode.lower() == "decrypt":
        shiftedPosition = initialPosition - key

def wrap():
    global shiftedPosition
    if shiftedPosition >= len(characters):
        shiftedPosition = shiftedPosition - len(characters)
    elif shiftedPosition < 0:
        shiftedPosition = shiftedPosition + len(characters)

# Main Program

print("Welcome to the Caesar Cipher!")

print("\nWhen using the cipher, please take note of the following accepted characters:")
print("    Letters: " + upper + lower)
print("    Numbers: " + numbers)
print("    Symbols: " + symbols)

print("\n-----------------------------------------------------------------------------")

initialMessage = input("\nPlease type or paste your message here:\n")
mode = input("\nWould you like to encrypt or decrypt your message?\n")
key = int(input("\nPlease select a key between 0 and 93: "))

for character in initialMessage:
    if character in characters:
        initialPosition = characters.find(character)
        cipher()
        wrap()
        
        shiftedMessage = shiftedMessage + characters[shiftedPosition]

    else:
        shiftedMessage = shiftedMessage + character

print("\nYour " + mode.lower() + "ed message is: \n" + shiftedMessage)
