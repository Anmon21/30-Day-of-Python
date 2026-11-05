# 1. Exception Handling
# Python uses try, except, else, and finally blocks to handle runtime errors gracefully
# and keep applications from crashing.

try:
    name = input('Enter your name: ')
    year_born = input('Year you were born: ')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occurred')
except ValueError:
    print('Value error occurred')
except ZeroDivisionError:
    print('Zero division error occurred')
else:
    print('I usually run with the try block')
finally:
    print('I always run.')


# 2. Unpacking Lists and Dictionaries
# Using the * operator for tuples/lists and ** for dictionaries to destructure arguments.

def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print("Sum of unpacked list:", sum_of_five_nums(*lst))  # 15

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)  # Finland Sweden Norway ['Denmark', 'Iceland']

def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'

dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
print(unpacking_person_info(**dct))


# 3. Packing Arguments
# Using *args and **kwargs to accept an arbitrary number of arguments or keyword arguments.

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print("Packed sum:", sum_all(1, 2, 3, 4, 5))  # 15

def packing_person_info(**kwargs):
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

packing_person_info(name="Asabeneh", country="Finland", city="Helsinki", age=250)


# 4. Spreading
# Combining lists using the spread operator (*).

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
combined_lst = [0, *lst_one, *lst_two]
print("Spread list:", combined_lst)


# 5. Enumerate
# Getting both the index and the item while looping through an iterable.

for index, country in enumerate(countries):
    if country == 'Finland':
        print(f'The country {country} has been found at index {index}')


# 6. Zip
# Combining multiple lists together during a loop.

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_veges = []

for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit': f, 'veg': v})

print("Zipped fruits and veggies:", fruits_and_veges)