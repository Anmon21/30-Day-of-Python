# Creating sets 
st = set()  # empty set
# Example 
st = {'banana', 'mango', 'orange', 'lemon'}
 # Sets lenght 
print(len(st))  # 4

# Checking an Item
print ('banana' in st)  # True
print ('lime' in st)    # False

# Adding Items
st.add('lime')  # add one item to the set
print(st)  # {'banana', 'mango', 'orange', 'lemon', 'lime'}
st.update(['apple', 'grape'])  # add multiple items to the set
print(st)  # {'banana', 'mango', 'orange', 'lemon', 'lime', 'apple', 'grape'}

# Removing Items from a Set
st.discard('banana')  # remove an item from the set
print(st)  # {'mango', 'orange', 'lemon', 'lime', 'apple', 'grape'}
st.remove('lime')  # remove an item from the set
print(st)  # {'mango', 'orange', 'lemon', 'apple', 'grape'}

# Clearing Items in a Set
st.clear()  # clear all items in the set
print(st)  # set()

# Deleting a Set
del st  # delete the set

# Converting Lists to Sets
fruits = ['banana', 'orange', 'mango', 'lemon',]
fruits = set(fruits)  # converting list to set
print(fruits)

# Joining Sets
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'}
fruits_and_vegetables = fruits.union(vegetables)  # join
print(fruits_and_vegetables)  # {'banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot'}

# Finding Intersection Items
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'Tomato', 'Potato', 'Cabbage','Onion', 'Carrot'}
fruits_and_vegetables = fruits.intersection(vegetables)  # join
print(fruits_and_vegetables)  # set() - no intersection

# Checking the Difference Between Two Sets 
whole_numbers = {0, 1, 2, 3, 4, 5}
even_numbers = {0, 2, 4}
odd_numbers = whole_numbers.difference(even_numbers)
print(odd_numbers)  # {1, 3, 5}

# Checking the Symmetric Difference Between Two Sets
whole_numbers = {0, 1, 2, 3, 4, 5}
even_numbers = {0, 2, 4}
odd_numbers = whole_numbers.symmetric_difference(even_numbers)
print(odd_numbers)  # {1, 3, 5}

# Joining Sets  
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}

