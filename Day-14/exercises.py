# Exercises Level 1

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Explain the difference between map, filter, and reduce.

# The map function applies a given function to every item in an iterable and returns an iterator containing the results.
# The filter function applies a given function to every item in an iterable and returns an iterator containing only the items for which the function returns True. 
# The reduce function applies a given function cumulatively to the items of an iterable, reducing the iterable to a single value.

# Explain the difference between higher order function, closure and decorator

# A higher order function is a function that takes one or more functions as arguments and/or returns a function as its result.
# A closure is a function that retains access to its lexical scope, even when the function is executed outside that scope.
# A decorator is a function that takes another function as an argument, adds some functionality to it, and returns a new function. 
# Decorators are often used to modify the behavior of functions or methods in a clean and readable way.


# Define a call function before map, filter or reduce, see examples.
# Defined functions
import numbers
from tkinter.font import names


def square(x):
    return x ** 2

def is_even(x):
    return x % 2 == 0

# Using them in higher-order functions
squared_numbers = list(map(square, numbers))
even_numbers = list(filter(is_even, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(even_numbers)     # [2, 4, 6, 8, 10]

# Use for loop to print each country in the countries list.

for country in countries:
    print(country)

# Use for loop to print each name in the names list.
for name in names:
    print(name)

# Use for loop to print each number in the numbers list.
for number in numbers:
    print(number)

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_countries = list(map(str.upper, countries))
# Use map to create a new list by changing each number to its square in the numbers list
squared_numbers = list(map(square, numbers))
# Use map to change each name to uppercase in the names list
uppercase_names = list(map(str.upper, names))
# Use filter to filter out countries containing 'land'.
countries_with_land = list(filter(lambda country: 'land' in country, countries))
# Use filter to filter out countries having exactly six characters.
six_char_countries = list(filter(lambda country: len(country) == 6, countries))
# Use filter to filter out countries containing six letters and more in the country list.
six_or_more_char_countries = list(filter(lambda country: len(country) >= 6, countries))
# Use filter to filter out countries starting with an 'E'
countries_starting_with_e = list(filter(lambda country: country.startswith('E'), countries))
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
chained_result = list(map(lambda x: x.upper(), filter(lambda x: 'land' not in x.lower(), countries)))
print(chained_result)
# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_lists(lst):
    return list(filter(lambda x: isinstance(x, str), lst))

mixed_list = ['Apple', 10, 'Banana', 3.14, True, 'Cherry']
print(get_string_lists(mixed_list))
# Use reduce to sum all the numbers in the numbers list.
from functools import reduce

total_sum = reduce(lambda x, y: x + y, numbers)
print(total_sum)  # 55
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
from functools import reduce

sentence = reduce(lambda x, y: f"{x}, {y}" if y != countries[-1] else f"{x}, and {y} are north European countries", countries)
print(sentence)
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).
def categorize_countries(country_list, pattern):
    return list(filter(lambda x: pattern.lower() in x.lower(), country_list))

# Example testing with 'land'
print(categorize_countries(countries, 'land'))
# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def count_countries_by_letter(country_list):
    result = {}
    for country in country_list:
        letter = country[0].upper()
        result[letter] = result.get(letter, 0) + 1
    return result

print(count_countries_by_letter(countries))
# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
def get_first_ten_countries(country_list):
    return country_list[:10]
# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(country_list):
    return country_list[-10:]

# Exercises: Level 3
# Sort countries by name, by capital, by population

from countries_data import countries_data

# Sort by name
sorted_by_name = sorted(countries_data, key=lambda x: x['name'])

# Sort by capital (handling missing capitals gracefully)
sorted_by_capital = sorted(countries_data, key=lambda x: x.get('capital', ''))

# Sort by population (descending order)
sorted_by_population = sorted(countries_data, key=lambda x: x['population'], reverse=True)

# Sort out the ten most spoken languages by location.

from collections import Counter

def most_spoken_languages(data):
    language_counter = Counter()
    for country in data:
        for language in country.get('languages', []):
            language_counter[language] += 1
    # Returns top 10 languages as a list of tuples: (language, count)
    return language_counter.most_common(10)

print(most_spoken_languages(countries_data))

# Sort out the ten most populated countries.
def most_populated_countries(data):
    sorted_countries = sorted(data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:10]

print(most_populated_countries(countries_data))