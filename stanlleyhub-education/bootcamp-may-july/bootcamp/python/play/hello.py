# # comments in python 

# """

# This is a multiline comment

# """

# # hello world
# print("Hello World")

# # Variables
# age = 10
# name = "Locke"
# print(f"My name is {name}  and age {age}")

# # Data Types
# """
# 1. str   eg "hello"  -text
# 2. int, float, complex   eg. 15, 14.56   ---numbers/numeric
# 3. list, tuple, range    ---sequence
# 4. dict  ---mapping
# 5. bool Yes/No True/False --bolean

# """

# # Built-in Python Data Types
# # Strings 

# hello = "Hello World" # double quotes
# hello = 'Hello World' #single quotes
# multi_string = """
# multiple line strings and literals
# """

# print(f"{hello}, {multi_string}")

# # Numbers 
# x = 4 #int -integer
# y = 2.8 #float 

# print(x, y)

# # boleans
# my_bool = True
# my_bool2 = False

"""strings slicing

m y b e a c o n
0 1 2 3 4 5 6 7
            -1
"""

string = "mybeacon"
string[0:1]
# print(string)


#inputs
# first_name = input("1. What is your 1st name: \n")
# second_name = input("2. What is 2nd your name: \n")
# age = input("3. What is your age: \n")
# school = input("4. Where do you study: \n")
# course = input("5. What course do you study: \n")
# current_year = input("6. What is your current year: \n")
# print(f"1.Your 1st name is: {first_name}\n 2. Your 2nd name is: {second_name} \n 3. Your age is {age} \n 4. You study at: {school} \n 5. Your course is: {course} \n 6. Your current year is: {current_year}")


""""
Python Functions
We use the def keyword to declare functions in python

def myfunc():
    name = 
    age =

myfunc()

"""

#Profile function
# def profile():
#     first_name = input("1. What is your 1st name: ")
#     second_name = input("\n2. What is 2nd your name: ")
#     age = input("\n3. What is your age: ")
#     school = input("\n4. Where do you study: ")
#     course = input("\n5. What course do you study: ")
#     current_year = input("\n6. What is your current year: ")
#     print(f"\n1.Your 1st name is: {first_name}\n 2. Your 2nd name is: {second_name} \n 3. Your age is {age} \n 4. You study at: {school} \n 5. Your course is: {course} \n 6. Your current year is: {current_year}")

# profile()



"""
Python conditions

if/else condition

"""

# num = int(input("Enter a number: "))

# if num > 100:
#     print(f"{num} is greater than 100.")
# else:
#     print(f"{num} is less than 100.")

"""
Python Loops
loops are used in python to run continuosly untils a given state is met

the for keyword is used to open loops
for name in range():
        funtion
else 
"""

# for item in range(6):
#     if item == 3:  continue
#     print(item)
# else: 
#     print("Finally finished")

"""
File handling in python 
Python can be used to interact with files txt, program files and so on. 

With keyword is used when  refrencing a file
"""

#file actions
with open("poem.txt", "a") as file:
    file.write("\nby Stanlley Locke  @2026")