# Create an empty dictionary called dog
dog = {}
#Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Mini'
dog['color'] = 'Golden yellow'
dog['breed'] = 'Spaniel'
dog['legs'] = 4
dog['age'] = 5
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'Bilguun',
    'last_name': 'Deleg',
    'gender': 'Male',
    'age': 19,
    'marital_status': False,
    'skills': ['Python', 'JavaScript', 'React'],
    'country': 'Mongolia',
    'city': 'Ulaanbaatar',
    'address': {
        'street': 'Peace Avenue',
    }
}
#Get the length of the student dictionary
print(len(student)) # 9
#Get the value of skills and check the data type, it should be a list
print(student['skills']) # ['Python', 'JavaScript', 'React']
print(type(student['skills'])) # <class 'list'>
#Modify the skills values by adding one or two skills
student['skills'].append('Node.js')
student['skills'].append('Django')
print(student['skills']) # ['Python', 'JavaScript', 'React', 'Node.js', 'Django']
#Get the dictionary keys as a list
print(student.keys()) # dict_keys(['first_name', 'last_name', 'gender', 'age', 'marital_status', 'skills', 'country', 'city', 'address'])
#Get the dictionary values as a list
print(student.values()) # dict_values(['Bilguun', 'Deleg', 'Male', 19, False, ['Python', 'JavaScript', 'React', 'Node.js', 'Django'], 'Mongolia', 'Ulaanbaatar', {'street': 'Peace Avenue'}])
#Change the dictionary to a list of tuples using items() method
print(student.items()) # dict_items([('first_name', 'Bilguun'), ('last_name', 'Deleg'), ('gender', 'Male'), ('age', 19), ('marital_status', False), ('skills', ['Python', 'JavaScript', 'React', 'Node.js', 'Django']), ('country', 'Mongolia'), ('city', 'Ulaanbaatar'), ('address', {'street': 'Peace Avenue'})])
#Delete one of the items in the dictionary
del student['address']
#Delete one of the dictionaries
del dog
