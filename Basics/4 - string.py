from importlib.metadata import distribution


string = "It is a text" #case-sensitive language
#there is a lot built-in method for string - some useful
print(string.upper()) #uppercase 
print(string.lower()) #lowercase
print(string.find('s')) #returns the index of the first character 's'
print(string.replace('is', '2')) #replaces the first str to the second

print("text" in string) #returns a boolean if 'text' can be found in string variable