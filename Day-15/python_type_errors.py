# When writing code, typos and mistakes happen. When code fails to run,
# Python displays a traceback message with information on where the problem
# occurred, the error type, and often suggestions for a fix.


# 1. SyntaxError
# Raised when the parser encounters invalid Python syntax.

# Incorrect:
# print 'hello world'  # SyntaxError: Missing parentheses in call to 'print'

# Correct:
print('hello world')


# 2. NameError
# Raised when a local or global variable name is not defined.

# Incorrect:
# print(age)  # NameError: name 'age' is not defined

# Correct:
age = 25
print(age)  # 25


# 3. IndexError
# Raised when trying to access a sequence index that is out of range.

numbers = [1, 2, 3, 4, 5]

# Incorrect:
# print(numbers[5])  # IndexError: list index out of range

# Correct:
print(numbers[4])  # 5


# 4. ModuleNotFoundError
# Raised when an import statement fails to find the specified module.

# Incorrect:
# import maths  # ModuleNotFoundError: No module named 'maths'

# Correct:
import math


# 5. AttributeError
# Raised when an attribute reference or assignment fails.

# Incorrect:
# print(math.PI)  # AttributeError: module 'math' has no attribute 'PI'

# Correct:
print(math.pi)  # 3.141592653589793


# 6. KeyError
# Raised when a dictionary key is not found.

user = {'name': 'Asab', 'age': 250, 'country': 'Finland'}

# Incorrect:
# print(user['county'])  # KeyError: 'county'

# Correct:
print(user['country'])  # Finland


# 7. TypeError
# Raised when an operation is applied to an object of an inappropriate type.

# Incorrect:
# result = 4 + '3'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Correct:
print(4 + int('3'))  # 7


# 8. ImportError
# Raised when an imported name cannot be found inside the module.

# Incorrect:
# from math import power  # ImportError: cannot import name 'power' from 'math'

# Correct:
from math import pow

print(pow(2, 3))  # 8.0


# 9. ValueError
# Raised when a function gets an argument of correct type but invalid value.

# Incorrect:
# number = int('12a')  # ValueError: invalid literal for int() with base 10: '12a'

# Correct:
print(int('12'))  # 12


# 10. ZeroDivisionError
# Raised when dividing or taking modulo by zero.

# Incorrect:
# result = 1 / 0  # ZeroDivisionError: division by zero

# Correct:
divisor = 2
print(1 / divisor)  # 0.5

# Quick Summary Reference
# SyntaxError         -> Typo/punctuation mistake      -> Fix syntax (e.g. add parentheses)
# NameError           -> Variable used before defined  -> Define the variable first
# IndexError          -> Index out of bounds           -> Check len(list) before indexing
# ModuleNotFoundError -> Incorrect module name         -> Fix spelling or install module
# AttributeError      -> Non-existent method/attribute -> Check docs for right attribute name
# KeyError            -> Missing dictionary key        -> Fix key spelling or use .get()
# TypeError           -> Incompatible types            -> Cast variables to matching types
# ImportError         -> Non-existent import name      -> Use correct function/variable name
# ValueError          -> Invalid value format          -> Clean/validate input before casting
# ZeroDivisionError   -> Dividing by zero              -> Ensure divisor != 0