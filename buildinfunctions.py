"""
Build in fuctions for the language:
    print: print the value of the expression
    input: read a line of input from the user and return it as a string
    int: convert a string to an integer
    str: convert an integer to a string
    len: return the length of a string
    range: return a list of integers from 0 to n-1
"""
#print function
print("Hello, World!")

#input function
name = input("What is your name? ")
print(f"Hello, {name}!")

#type functions
num_str = "123"
num_int = int(num_str)
type(num_int)  # Output: <class 'int'>

#int
num = int(4.56)
#float
#str
#tuple
#list

#abs
abs(-5)  # Output: 5

#pow
pow(2, 3)  # Output: 8

#min/max
min(5, 10)  # Output: 5
max(5, 10)  # Output: 10

#round
round(3.14159, 2)  # Output: 3.14

#divmod
divmod(10, 3)  # Output: (3, 1)

#bin/oct/hex
bin(10)  # Output: '0b1010'
oct(10)  # Output: '0o12'
hex(10)  # Output: '0xa'

#id
x = 10
id(x)  # Output: memory address of x

#ord
ord('A')  # Output: 65

#len
len("Hello")  # Output: 5

#sum
sum([1, 2, 3])  # Output: 6

#help
help(print)  # Output: documentation for the print function

