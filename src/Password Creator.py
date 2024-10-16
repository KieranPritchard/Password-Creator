import random
import string

# Varibles for all ascii key characters and characters for password generation
upper_case_letters = string.ascii_uppercase
lower_case_letters = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

characters = upper_case_letters + lower_case_letters + numbers + symbols

# Generate password function it makes a password with a length of 12 characters

def Generate_Password(characters):

    password = ""

    for i in range(12):
        password += random.choice(characters)

    return password

# Outputs the password that gets generated 

print("Your Password: " + Generate_Password(characters))