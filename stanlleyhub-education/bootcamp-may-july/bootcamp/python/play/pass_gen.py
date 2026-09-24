# modules
import math
import random

# declare funtion
def generatePassword(length = 12 ):
    uperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers =  "0123456789"
    symbols = r"!@#$%^&*()_+=,.;'/;]\[]"

    allChars = uperCase + lowerCase.lower() + numbers + symbols
    # print(allChars)


    password = ""

    for letter in range(length):
        password += random.choice(allChars)
        # print(password)

    return password


def saveToFile(password, filename="password.txt"):
    with open(filename, "a") as file:
        file.write(password + "\n")
    
    print(f"--> Saved '{password}' to {filename}\n")



new_password = generatePassword()
print(new_password)
saveToFile(new_password)