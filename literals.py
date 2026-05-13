'''
Literals are fixed values that are directly written into the code. They can be of various types, such as strings, numbers, booleans, etc. In Python, literals are used to represent data in a human-readable form.
Here are some examples of different types of literals in Python:
String Literals
String literals are enclosed in either single quotes (' ') or double quotes (" "). They can contain letters
, digits, and special characters. For example:
name = "John Doe"
greeting = 'Hello, World!'
Numeric Literals
Numeric literals represent numbers and can be of different types, such as integers, floating-point numbers,
and complex numbers. For example:
age = 30
pi = 3.14
complex_number = 1 + 2j
Boolean Literals
Boolean literals represent the truth values True and False. They are used in logical operations and conditional statements
is_valid = True
is_empty = False
None Literal
The None literal represents the absence of a value or a null value. It is often used to
indicate that a variable has no value or to signify the end of a list or a function that does not return anything.
result = None
In summary, literals are a fundamental part of programming in Python, allowing us to represent data directly
in our code. They can be of various types, including strings, numbers, booleans, and None.
'''
# String literals
name = "John Doe"
greeting = 'Hello, World!'


# Numeric literals
age = 30
pi = 3.14
a = 0b1010  # Binary literal (10 in decimal)
b = 0o755   # Octal literal (493 in decimal)
c = 0xFF    # Hexadecimal literal (255 in decimal)
d = 0x12c     # Hexadecimal literal (300 in decimal)

# float literals
float1 = 1.23
float2 = 1.5e-3  # This is equivalent to 1.5 * 10^-3 or 0.0015
float3 = 1.5e+3  # This is equivalent to 1.5 * 10^3 or 1500.0
complex_number = 1 + 2j
# Boolean literals
is_valid = True
is_empty = False

# String literals with escape characters
string= "This is a string"
string_with_quote = 'It\'s a nice day!'  # Using escape character to include a single quote
print(string_with_quote)
unicode = u"\u00A9 2026"  # Unicode string literal representing the copyright symbol
print(unicode)
raw_string = r"C:\Users\JohnDoe\Documents"  # Raw string literal to avoid escaping backslashes
print(raw_string)
escaped_string = "This is a string with a newline character.\nAnd this is on a new line."
print(escaped_string)

# None literal
result = None


print(name)           # Output: John Doe
print(greeting)       # Output: Hello, World!
print(age)            # Output: 30
print(pi)             # Output: 3.14
print(complex_number) # Output: (1+2j)
print(is_valid)       # Output: True
print(is_empty)       # Output: False
print(result)         # Output: None
print(a)              # Output: 10
print(b)              # Output: 493
print(c)              # Output: 255
print(d)              # Output: 300
print(float1)         # Output: 1.23
print(float2)         # Output: 0.0015
print(float3)         # Output: 1500.0