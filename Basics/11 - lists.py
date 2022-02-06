names = ["Anne","Bob","Tom", "Adam", "Katrine"] # create a list of string
print(names) #prints all elements of the list
print(names[0]) #prints the 0 element of the list only, it is 'Anne'
print(names[-1]) # prints the last element of the list, it is 'Katrine'
print(names[-2]) # prints the second last element of the list, it is 'Adam'

names[1] = "Charlie" # change the value of an exact element in the list
print(names)

print(names[0:3]) # prints all elements of the list which can be found between 0 and 3, 0th element is printed but the 3rd is not printed, like '0 < 3'



#list methods
numbers = [1,2,3,4,5] # create a list of numbers with 5 elements, indexed 0 to 4
numbers.append(6) # append the number '6' to the end of the 'numbers' list
print(numbers)

numbers.insert(0,99) # insert an element to an exact position in the list, insert '99' to position(index) 0, does NOT deletes the current element of index 0 but pushes the whole list
print(numbers)

numbers.remove(3) # removes a value from the list, does not care about its position(index)
print(numbers)

numbers.clear() # clears the whole list
print(numbers)

numbers = [1,2,3,4,5]
print(1 in numbers) # like an if, checks the numbers list and if there is a '1' returns True else False

print(len(numbers)) # returns the number of elements in the list, (len = length) 