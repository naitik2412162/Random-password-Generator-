#---------------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Naiti
#
# Created:     26-03-2026
# Copyright:   (c) Naiti 2026
# Licence:     <your licence>
#---------------------------------------------------------------------------------------
import random
import string

print("=== Password Generator (Letters + Numbers Only) ===")

name = input("Enter your first name: ")
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits

password = ""

for i in range(length):
    password += random.choice(characters)

final_password = name.capitalize() + password

print("\nSuggested Password:", final_password)