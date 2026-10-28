# filter only negative and zero in the list using list comprehension
numbers = [1, 2, 3, 4, 5, -1, -2, -3, 0]
negative_numbers = [num for num in numbers if num <= 0]
print(negative_numbers)  # [-1, -2, -3, 0]

# Flatten the following list of lists of integers using list comprehension
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for sublist in list_of_lists for num in sublist]
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# using list comprehension create the following list of tuples:
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
list_of_tuples = [(i, j) for i in range(3) for j in range(3)]
print(list_of_tuples) 

# Flatten the following list into a new list using list comprehension
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flat_countries = [country for sublist in countries for country in sublist]
print(flat_countries)  # [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]

# Change the following list of lists of languages into a flat list using list comprehension.
# [['Python', 'Java'], ['JavaScript', 'Ruby'], ['C++', 'C#']]
languages = [['Python', 'Java'], ['JavaScript', 'Ruby'], ['C++', 'C#']]
flat_languages = [language for sublist in languages for language in sublist]
print(flat_languages)  # ['Python', 'Java', 'JavaScript', 'Ruby', 'C++', 'C#']

# change the following list of lists to a list of concatenated strings
# [['Python', 'Java'], ['JavaScript', 'Ruby'], ['C++', 'C#']]
languages = [['Python', 'Java'], ['JavaScript', 'Ruby'], ['C++', 'C#']]
concatenated_languages = [' '.join(sublist) for sublist in languages]
print(concatenated_languages)  # ['Python Java', 'JavaScript Ruby', 'C++ C#']

# Lambda function which can solve a slope or y intercept of a linear equation
# y = mx + b
slope = lambda m, x: m * x
y_intercept = lambda b: b