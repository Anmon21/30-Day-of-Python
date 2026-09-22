# Condition
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number

# if Else
a = 3
if a > 0:
    print('A is a positive number')
else:
    print('A is a negative number')
# A is a positive number

# if elif else
a = 3
if a > 0:
    print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')
# A is a positive number    

# Shorthand if else
a = 3
print('A is a positive number') if a > 0 else print('A is a negative number')
# A is a positive number

#Nested if else
a = 3
if a > 0:
    if a < 10:
        print('A is a positive single digit number')
    else:
        print('A is a positive number but not a single digit')
else:
    print('A is a negative number')


# If Condition and Logical Operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

# If and Or Logical Operators

user = 'Anmon'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
    