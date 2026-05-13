"""
Keywords
========
Keywords are reserved words that have a special meaning in Python. They cannot be used as identifiers (variable names, function names, etc.). Here is a list of Python keywords:
Python has 35 keywords as of version 3.10, and they are:
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield

Identifiers
===========
Identifiers are names used to identify variables, functions, classes, modules, and other objects in Python. They must follow certain rules:
1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
2. An identifier cannot start with a digit.
3. An identifier cannot be a keyword.
4. An identifier is case-sensitive (e.g., myVariable and myvariable are different identifiers).
5. An identifier should be descriptive and meaningful to improve code readability.

Examples of valid identifiers:
my_variable
myVariable
my_variable_2

Examples of invalid identifiers:
2my_variable  # starts with a digit
my-variable   # contains a hyphen
my variable   # contains a space

"""

import keyword
print(keyword.kwlist)  # prints the list of Python keywords

