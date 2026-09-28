# While loop
count = 0
while count < 5:
    print(count)
    count += 1

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

# Break and Continue
count = 0
while count < 5:
    if count == 3:
        break
    print(count)
    count += 1
    