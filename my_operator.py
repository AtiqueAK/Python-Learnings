"""
operators in Python
Operators are special symbols or keywords that perform specific operations on one or more operands (values or variables). They are used to manipulate data and perform various computations in Python. There are several types of operators in Python, including:
1. Arithmetic Operators: These operators perform basic mathematical operations such as addition (+), subtraction (-), multiplication (*), division (/), modulus (%), exponentiation (**), and floor division (//).
2. Comparison Operators: These operators compare two values and return a boolean result (True or False). Examples include equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).
3. Logical Operators: These operators are used to combine multiple boolean expressions. They include and, or, and not.
4. Assignment Operators: These operators are used to assign values to variables. Examples include the simple assignment operator (=) and compound assignment operators like +=, -=, *=, /=, etc.
5. Bitwise Operators: These operators perform bit-level operations on integers. Examples include bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise NOT (~), left shift (<<), and right shift (>>).
6. Identity Operators: These operators are used to compare the memory locations of two objects. They include is and is not.
7. Membership Operators: These operators are used to check if a value is present in a sequence (like a list, tuple, or string). They include in and not in.
In summary, operators are essential components of Python that allow us to perform various operations on data and variables. Understanding how to use these operators effectively is crucial for writing efficient and readable code in Python.
"""

# Arithmetic Operators
a = 10
b = 5
print(a + b)  # Addition: 15
print(a - b)  # Subtraction: 5
print(a * b)  # Multiplication: 50
print(a / b)  # Division: 2.0
print(a % b)  # Modulus: 0
print(a ** b) # Exponentiation: 100000
print(a // b) # Floor Division: 2

# Comparison Operators
print(a == b)  # Equal to: False
print(a != b)  # Not equal to: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater than or equal to: True
print(a <= b)  # Less than or equal to: False

# Logical Operators
x = True
y = False
print(x and y)  # Logical AND: False
print(x or y)   # Logical OR: True
print(not x)    # Logical NOT: False

# Bitwise Operators
m = 5  # In binary: 0101
n = 3  # In binary: 0011
print(m & n)  # Bitwise AND: 1 (In binary: 0001)
print(m | n)  # Bitwise OR: 7 (In binary: 0111)
print(m ^ n)  # Bitwise XOR: 6 (In binary: 0110)
print(~m)     # Bitwise NOT: -6 (In binary: 1010)
print(m << 1) # Left Shift: 10 (In binary: 1010)
print(m >> 1) # Right Shift: 2 (In binary: 0010)

# Assignment Operators
c = 10
c += 5  # Equivalent to c = c + 5
print(c)  # 15
c -= 3  # Equivalent to c = c - 3
print(c)  # 12
c *= 2  # Equivalent to c = c * 2
print(c)  # 24
c /= 4  # Equivalent to c = c / 4
print(c)  # 6.0

# Identity Operators
list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)  # True, because both variables point to the same object in memory
print(list1 is not list2)  # False, because both variables point to the same object in memory
list3 = [1, 2, 3]
print(list1 is list3)  # False, because list1 and list3 are different objects in memory
print(list1 == list3)  # True, because list1 and list3 have the same content

# Membership Operators
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  # True, because 'banana' is in the list
print('grape' in fruits)   # False, because 'grape' is not in the list
print('grape' not in fruits)  # True, because 'grape' is not in the list

