import math
import random

# generate password funtion
def generatePassword(length = 12):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowecase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = r"!@#$%^&*()_+=,.;'/;]\[]"

    # combine characters to one single string
    allChars = uppercase + lowecase.lower() + numbers + symbols
    print(lowecase.lower())

    password = ""

    #loop length times the default number 12 to build a password
    for _ in range(length):
        #pythons choice() to pick random characters
        password += random.choice(allChars)

    return password

my_password = generatePassword()
print(my_password)