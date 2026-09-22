#Exercises: Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies

print(len(it_companies))

#Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['Tesla', 'SpaceX'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('Facebook')
print(it_companies)

#What is the difference between remove and discard
# `remove` will raise an error if the item is not found, while `discard` will not.

# Exercises: Level 2
# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
D = A.intersection(B)
print(D)

#Is A subset of B
E = A.issubset(B)
print(E)

#Are A and B disjoint sets
F = A.isdisjoint(B)
print(F)

#Join A with B and B with A
G = A.union(B)
H = B.union(A)
print(G)
print(H)
#What is the symmetric difference between A and B
I = A.symmetric_difference(B)
print(I)
#Delete the sets completely
del C

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print("Length of the list:", len(age))
print("Length of the set:", len(age_set))

#Explain the difference between the following data types: string, list, tuple and set
#string: A string is a sequence of characters enclosed in quotes. It is immutable, meaning it cannot be changed after creation.
#list: A list is an ordered collection of items that can be of different data types. It is mutable, meaning it can be changed after creation.
#tuple: A tuple is similar to a list, but it is immutable. It is an ordered collection of items that can be of different data types.
#set: A set is an unordered collection of unique items. It is mutable, meaning it can be changed after creation.


#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
words = sentence.split()
unique_words = set(words)
print("Number of unique words:", len(unique_words))

