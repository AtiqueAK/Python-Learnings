"""
Loops are used to repeat a block of code until a certain condition is met. In Python, there are two main types of loops: for loops and while loops.
A while loop continues to execute a block of code as long as a specified condition is true. The syntax for a while loop is as follows:

while condition:
    # code to be executed
"""
num = int(input("Enter a number: "))
i = 1
while i<11:
    print(num, "*", i, "=", num * i)
    i += 1