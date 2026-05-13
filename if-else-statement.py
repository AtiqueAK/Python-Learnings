"""
If-Else Statement in Python
The if-else statement is a fundamental control flow structure in Python that allows you to execute different blocks of code based on certain conditions. It is used to make decisions in your code and can help you handle different scenarios effectively.
The basic syntax of an if-else statement is as follows:
if condition:
    # Code to execute if the condition is true
else:
    # Code to execute if the condition is false
    # You can also use elif (short for "else if") to check multiple conditions:
    # elif another_condition:
    #   # Code to execute if another_condition is true
    # else:
    #  # Code to execute if all conditions are false
"""
# Example of an if-else statement


#Email: email@mail.com
#Password: password123
email = input("Enter your email: ")
password = input("Enter your password: ")

if email == "email@mail.com" and password == "password123":
    print("Login successful!")

elif email == "email@mail.com" and password != "password123":
    print("Incorrect password. Please try again.")
    password = input("Enter your password again: ")
    if password == "password123":
        print("Login successful!")
    else:
        print("Incorrect password. Please try again later.")
else:
    print("Invalid email or password. Please try again.")
