"""
Type Conversion
This code demonstrates how to convert between different data types in Python.
In Python, you can convert between different data types using built-in functions such as int(), float(), str(), etc. This process is known as type conversion or type casting.
In this example, we will convert a string to an integer, a float to an integer,
and an integer to a string. We will also demonstrate how to handle invalid type conversions using try-except blocks.

implicit type conversion (type coercion) is when Python automatically converts one data type to another during an operation. For example, when you add an integer and a float, Python will automatically convert the integer to a float before performing the addition.
explicit type conversion (type casting) is when you manually convert one data type to another using built-in functions. For example, you can use the int() function to convert a string to an integer, or the str() function to convert an integer to a string.

"""
# Converting a string to an integer
str_num = "10"
int_num = int(str_num)
print(int_num)  # Output: 10

# Converting a float to an integer
float_num = 3.14
int_num = int(float_num)
print(int_num)  # Output: 3

# Converting an integer to a string
int_num = 42
str_num = str(int_num)
print(str_num)  # Output: "42"


list('Hello')  # ['H', 'e', 'l', 'l', 'o']

set('Hello')   # {'H', 'e', 'l', 'o'}

# Example of implicit type conversion
a = 5
b = 3.14
result = a + b  # a is implicitly converted to a float before addition
print(result)  # Output: 8.14
type(result)  # Output: <class 'float'>

# Example of explicit type conversion with error handling
str_num = "abc"  # This is not a valid number
try:
    int_num = int(str_num)
    print(int_num)
except ValueError:
    print("Cannot convert the string to an integer. Please provide a valid number.")