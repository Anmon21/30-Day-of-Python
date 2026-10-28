# List Comprehension

# example 1: Create a list of numbers from 0 to 9
numbers = [i for i in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# example 2: Create a list of squares from 0 to 9
squares = [i ** 2 for i in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lambda function
# example 1: Create a list of numbers from 0 to 9 using lambda function
numbers = list(map(lambda x: x, range(10)))
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Lambda function inside another function
def square(x):
    return x ** 2

squares = list(map(square, range(10)))
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]