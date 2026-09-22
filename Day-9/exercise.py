#Exercises: Level 1

# 1

# Get user input using input(“Enter your age: ”). 
from ast import If


age = int(input("Enter your age: "))
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
if age >= 18:
    print("You are old enough to drive.")

else:
    years_left = 18 - age
    print(f"You need {years_left} more years to learn to drive.")


#2

#Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input.
#  You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. 
your_age = int(input("Enter your age: "))
my_age = 19 

if my_age > your_age:
    diff = my_age - your_age
    if diff >= 1:
        print(f"You are {diff} year younger than me.")

elif your_age > my_age:
    diff = your_age - my_age
    if diff >= 1:
        print(f"I am {diff} years older than you.")
else:
    print("We are the exact same age!")

#3

#Get two numbers from the user using input prompt. 
# If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print(f"{a} is greater than {b}.")
elif a < b:
    print(f"{a} is smaller than {b}.")
else:
    print(f"{a} is equal to {b}.")

# Exercises: Level 2

#4

# Write a code which gives grade to students according to theirs scores
score = int(input("Enter your score: "))
if score >= 90:
    print("A")

elif score >= 80 and score <= 89:
    print("B")
elif score >= 70 and score <= 79:
    print("C")
elif score >= 60 and score <= 69:
    print("D")
else:
    print("F")


#5
#Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter.
#March, April or May, the season is Spring June, July or August, the season is Summer

season = input("Enter the month: ").strip().title()
if season in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif season in ['December', 'January', 'February']:
    print("The season is Winter.")
elif season in ['March', 'April', 'May']:
    print("The season is Spring.")
elif season in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered.")


#6

#The following list contains some fruits:

#fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("Enter a fruit: ").strip().lower()
if fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(fruit)
    print("Modified list of fruits:", fruits)

#Exercises: Level 3
person = {
    'first_name': 'Bilguun',
    'last_name': 'Deleg',
    'age': 19,
    'country': 'Mongolia',
    'is_married': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'Typescript'],
    'address': {
        'street': 'Usnii gudamj',
        'zipcode': '11111'
    }
}

# 1. Check for 'skills' key and print the middle skill
if 'skills' in person and person['skills']:
    skills = person['skills']
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

# 2. Check for 'skills' key and check if 'Python' is in it
if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("Has Python skill:", has_python)

# 3. Determine developer role based on skills
if 'skills' in person:
    # Convert skills list to a set for exact or subset checking
    skills_set = set(person['skills'])

    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("unknown title")

# 4. Check if married and lives in Mongolia
# Pull directly using keys from the person dictionary
if person['country'] == 'Mongolia':
    status = "is married" if person['is_married'] else "is not married"
    
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He {status}.")