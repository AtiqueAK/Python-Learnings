"""
Python Support 3 categories of data types:
    1. Numeric data types: int, float, complex, bool and str
    2. Sequence data types: list, tuple, range
    3. Mapping data type: dict
    4. user defined data types: class
"""
# Numeric data types
a = 10
b = 3.14
c = 1 + 2j
d = True
e = "Hello, World!"
f = [1, 2, 3, 4, 5]
g = (1, 2, 3, 4, 5)
h = {1,2,3,4,5}
i = {"name": "John", "age": 30, "city": "New York"}


print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>
print(type(c))  # <class 'complex'>
print(type(d))  # <class 'bool'>
print(type(e))  # <class 'str'>
print(type(f))  # <class 'list'>
print(type(g))  # <class 'tuple'>
print(type(h))  # <class 'set'>
print(type(i))  # <class 'dict'>
print(1e308)    # 1e+308 heigest value printable in python
print(1e-308)   # 1e-308 lowest value printable in python
