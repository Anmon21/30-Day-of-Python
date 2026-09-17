# Variables in Python

first_name = 'Bilguun'
last_name = 'Deleg'
country = 'Mongolia'
city = 'Ulaanbaatar'
age = 19
is_married = False
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname': 'Bilguun',
    'lastname': 'Deleg',
    'country': 'Mongolia',
    'city': 'Ulaanbaatar'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Bilguun', 'Deleg', 'Mongolia', 19, False

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)