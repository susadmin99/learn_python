numbers = range(5)  # generates numbers from 0 to 4, 5 is excluded
print(numbers)  # can't print out the range only the 'definition' of it

for num in numbers:  # prints out the whole range
    print(num)  # 0, 1, 2, 3, 4

numbers = range(10, 15)  # generates numbers from 10 to 14, 15 is excluded
for num in numbers:
    print(num)  # 10, 11, 12, 13, 14


# generates every second number from 10 to 15 because the step is 2(third parameter), 15 is excluded
numbers = range(10, 15, 2)
for num in numbers:
    print(num)  # 10, 12, 14

# range can be added to the for, does not need to be declared before
for num in range(5):
    print(num)  # 0, 1, 2, 3, 4
