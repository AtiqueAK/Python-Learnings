"""
Break, Continue, and Pass in Python
In Python, break, continue, and pass are control flow statements that are used to manage the flow of loops and conditional statements. They allow you to alter the normal execution of a loop or a block of code based on certain conditions.
1. Break: The break statement is used to exit a loop prematurely when a certain condition is met. When the break statement is executed, the loop is terminated, and the program continues with the next statement after the loop.
2. Continue: The continue statement is used to skip the current iteration of a loop and move
to the next iteration. When the continue statement is executed, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds to the next iteration.
3. Pass: The pass statement is a placeholder that does nothing. It is used when a statement is syntactically required but you do not want to execute any code. It can be useful in situations where you want to define a function or a class but have not implemented it yet.
In summary, break, continue, and pass are important control flow statements in Python that allow you to manage the execution of loops and conditional statements effectively. Understanding how to use these statements can help you write more efficient and readable code.
"""

# Example of break statement
for i in range(1, 11):
    if i == 5:
        break  # This will exit the loop when i is 5
    print(i)

# Example of continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue  # This will skip the rest of the code for even numbers
    print(i)

# Example of pass statement
def my_function():
    pass  # This is a placeholder for future code
