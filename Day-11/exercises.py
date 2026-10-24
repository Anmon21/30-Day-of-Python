# Declare a function add_two_numbers which takes two numbers as parameters and returns the sum of the two numbers.


from ast import keyword
import math


def add_two_numbers(num1, num2):
    return num1 + num2

# Area of a circle is calculated as follows: area = π x r x r. Write a function which calculates area_of_circle.
def area_of_circle(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for num in args:
        if isinstance(num, (int, float)):
            total += num
        else:
            return "All arguments must be numbers."
    return total

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to_fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    month = month.strip().title()
    if month in ['September', 'October', 'November']:
        return "Autumn"
    elif month in ['December', 'January', 'February']:
        return "Winter"
    elif month in ['March', 'April', 'May']:
        return "Spring"
    elif month in ['June', 'July', 'August']:
        return "Summer"
    else:
        return "Invalid month entered."

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined (vertical line)."
    return (y2 - y1) / (x2 - x1)

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.


def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real solutions."
    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(my_list):
    for item in my_list:
        print(item)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(my_list):
    reversed_list = []
    for item in my_list:
        reversed_list.insert(0, item)
    return reversed_list

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(my_list):
    capitalized_list = []
    for item in my_list:
        capitalized_list.append(item.capitalize())
    return capitalized_list

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(my_list, item):
    my_list.append(item)
    return my_list

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(n):
    total = 0
    for i in range(n + 1):
        if i % 2 != 0:
            total += i
    return total

# Declare a function named sum_of_evens. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(n):
    total = 0
    for i in range(n + 1):
        if i % 2 == 0:
            total += i
    return total

# Exercises: Level 2

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(n):
    evens = 0
    odds = 0
    for i in range(n + 1):
        if i % 2 == 0:
            evens += 1
        else:
            odds += 1
    return evens, odds

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if param:
        return False
    else:
        return True

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(numbers):
    if not numbers:
        return "List is empty."
    return sum(numbers) / len(numbers)

# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
def greet(name="Guest"):
    return f"Hello, {name}!"

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values

def show_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Exercises: Level 3

# Write a function called is_prime, which checks if a number is prime. 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Write a functions which checks if all items are unique in the list.
def are_all_items_unique(my_list):
    return len(my_list) == len(set(my_list))
# Write a function which checks if all the items of the list are of the same data type.
def are_all_items_same_type(my_list):
    if not my_list:
        return True
    first_type = type(my_list[0])
    for item in my_list:
        if type(item) != first_type:
            return False
    return True

# Write a function which check if provided variable is a valid python variable
def is_valid_variable(var):
    return var.isidentifier() and not keyword.iskeyword(var)

# Create a function called most_spoken_languages that returns the 10 or 20 most spoken languages in the world in descending order from countries-data.py
def most_spoken_languages():
    from countries_data import countries_data
    language_count = {}
    for country in countries_data:
        for language in country['languages']:
            if language in language_count:
                language_count[language] += 1
            else:
                language_count[language] = 1
    sorted_languages = sorted(language_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_languages[:10]  # Return top 10 most spoken languages

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.
def most_populated_countries():
    from countries_data import countries_data
    sorted_countries = sorted(countries_data, key=lambda x: x['population'], reverse=True)
    return sorted_countries[:10]  # Return top 10 most populated countries