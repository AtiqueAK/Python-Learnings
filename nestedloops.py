"""
Nested Loops: A nested loop is a loop inside another loop. The inner loop will be executed for each iteration of the outer loop.
The syntax for nested loops is as follows:
for variable in sequence:
    for variable in sequence:
        # code to be executed
"""
"""
*
**
***
****
*****
"""

# Example of nested loops
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    for j in range(0,i):
        print("*", end=" ")
    print("")  # Move to the next line after each row