# Exercises: Level 1
# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and your brothers
sisters = ('Misheel', 'Enkh-chimeg', 'Enkh-jargal')
brothers = ('todbayar', 'Usukhjargal')

# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers

# 4. How many siblings do you have?
print(len(siblings))

# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('Deleg')
family_members.append('Dolgortseren')
family_members = tuple(family_members)  # Convert back to tuple

print(family_members)



# Exercises: Level 2
# 1. Unpack siblings and parents from family_members
family_members = ('Misheel', 'Enkh-chimeg', 'Enkh-jargal', 'todbayar', 'Usukhjargal', 'Deleg', 'Dolgortseren')
siblings, parents = family_members[:5], family_members[5:]
print(siblings)
print(parents)
# Create friuts, vegetables, animal products and food tuples. Join the tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk', 'Eggs', 'Meat')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = food_stuff_lt[middle_index:middle_index + 1]
print(middle_items)

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]
print(first_three_items)
print(last_three_items)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple: Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) #False
