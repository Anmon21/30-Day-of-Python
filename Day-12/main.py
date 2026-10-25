import mymodule
print(mymodule.generate_full_name('Bilguun', 'Deleg'))

from mymodule import generate_full_name
print(generate_full_name('Bilguun', 'Deleg'))

# Importing Functions from a Module and Renaming it
from mymodule import generate_full_name as fullname
print(fullname('Bilguun', 'Deleg'))

# Import Built-in Modules
import math
print(math.pi)
print(math.sqrt(2))
print(math.ceil(2.6))
print(math.floor(2.16))

# Sys module
import sys
print('Welcome {}. Enjoy 30 Days of Python Challenge.'.format(sys.argv[1]))

# String Module
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
