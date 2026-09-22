# Creating a Dictionary
person = {
    'first_name': 'Bilguun',
    'last_name': 'Deleg',
    'age': 19,
    'country': 'Mongolia',
    'is_married': False,
    'skills': ['Javascript', 'Node', 'JS', 'React', 'Python'],
    'address': {
        'Country': 'Mongolia',
        'City': 'Ulaanbaatar'
    }
}

# Dictionary Length
print(len(person))  # 7

# Accessing Values in Dictionary
print(person['first_name'])  # Bilguun
print(person['last_name'])  # Deleg
print(person['age'])  # 19
print(person['country'])  # Mongolia
print(person['is_married'])  # False
print(person['skills'])  # ['Javascript', 'Node', 'JS', 'React', 'Python']
print(person['address'])  # {'Country': 'Mongolia', 'City': 'Ulaanbaatar'}
print(person['address']['City'])  # Ulaanbaatar

# Adding new values to the Dictionary
person['title'] = 'Developer'
person['skills'].append('HTML')
print(person['title'])  # Developer
print(person['skills'])  # ['Javascript', 'Node', 'JS', 'React', 'Python', 'HTML']

# Modifying Items in a Dictionary
person['age'] = 20
print(person['age'])  # 20

# checking if a key exists in a Dictionary
print('first_name' in person)  # True
print('gender' in person)  # False

# Removing Items from a Dictionary
del person['is_married']
print(person['is_married'])  # This should give: KeyError: 'is_married'

# Changing Dictionary to a List of Items
person_items = person.items()
print(person_items)  # dict_items([('first_name', 'Bilguun'), ('last_name', 'Deleg'), ('age', 20), ('country', 'Mongolia'), ('skills', ['Javascript', 'Node', 'JS', 'React', 'Python', 'HTML']), ('address', {'Country': 'Mongolia', 'City': 'Ulaanbaatar'}), ('title', 'Developer')])

# Clearing a Dictionary
person.clear()
print(person)  # {}

# Deleting a Dictionary
del person