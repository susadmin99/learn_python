birth_year = input("Enter your birth year: ")
# convert birth_year(str) to int and store it in 'age'
age = 2022 - int(birth_year)
print(age)

# more converters
int()
float()
bool()
str()

# exercise
first = float(input("First: "))  # typecast can be at input
second = input("Second: ")
sum = first + float(second)  # typecast can be at usage
print("Sum: " + str(sum))  # float cannot concatenate with str
