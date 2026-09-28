#Exercises: Level 1
#Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
for count in range(0, 11):
    print(count)

#Iterate 10 to 0 using for loop, do the same using while loop.
count = 10
while count >= 0:
    print(count)
    count -= 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
for i in range(1, 8):
    print('#' * i)

#Use nested loops to create the following:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()

# Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(11):
    print(f"{i} x {i} = {i * i}")


#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
programming_languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in programming_languages:
    print(language)

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(101):
    if i % 2 == 0:
        print(i)

#Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(101):
    if i % 2 != 0:
        print(i)

#Exercises: Level 2'
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_of_numbers = 0
for i in range(101):
    sum_of_numbers += i
print(f"The sum of all numbers from 0 to 100 is: {sum_of_numbers}")

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_of_evens = 0
sum_of_odds = 0
for i in range(101):
    if i % 2 == 0:
        sum_of_evens += i
    else:
        sum_of_odds += i
print(f"The sum of all even numbers from 0 to 100 is: {sum_of_evens}")
print(f"The sum of all odd numbers from 0 to 100 is: {sum_of_odds}")
