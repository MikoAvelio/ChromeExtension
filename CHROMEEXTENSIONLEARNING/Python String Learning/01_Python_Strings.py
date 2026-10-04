#LEARNING NOTES

#Strings in python are surrounded by either single quotation marks, or double quotation marks.
#Some examples:
#print("Hello, World!")
#print('Hello, World!')

#--------------------------------------------------------------------------------

#Quotes inside Quotes
#You are able to use quotes inside a singular string as long as they dont match the quotes wrapping the string
# print("Hello, what is your name?")
# print("My name is 'Miko'.")
#OR
# print('My name is "Miko".')

#--------------------------------------------------------------------------------

#Assigning Strings to Variables
#Assign strings to variables, and then use the variable name to refer to the string

# x = "Hello, World!"
# y = 'Hello, World!'
# print(x)
# print(y)

#--------------------------------------------------------------------------------

# Multiline Strings
#Using three quotes allows for strings to span multiple lines
#Example:
# a = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."""
# print(a)
#OR
# a = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
# sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'''
# print(a)

#--------------------------------------------------------------------------------

#Strings are Arrays
#Similar to other languages, strings in Python are arrays of characters.
#But, Python does not have a character data type, a single character is simply a string with a length of 1.
#Square brackets can be used to slice elements of the string.

#Example:
# a = "Personal Project"
# print(a[0])
# print(a[1])
# print(a[2])
# print(a[3])
# print(a[4])
# print(a[5])
# print(a[6])
# print(a[7])

#--------------------------------------------------------------------------------

#Looping Through a String
#Since strings are arrays,
#this allows it to be able to loop through the characters in a string using a for loop.

# for x in "Personal Project":
#   print(x)

#--------------------------------------------------------------------------------

# String Length
#Use the len() function to return the length of a string.
# 
# a = "Personal Project"
# print(len(a))

#--------------------------------------------------------------------------------

#Check String
#To be able to check if a certain phrase or character is inside a string
#We must use the keyword in.

#Example:
# a = "Personal Project"
# print("Personal" in a)

#If using in if statement:
# a = "Personal Project"
# if "Personal" in a:
#     print("Yup thats correct")

#Check if NOT
#We use the keywords not in to check if a certain phrase or character is NOT present in a string.
#Example:
# a = "Personal Project"
# print("Miko" not in a)

# in if statement:
# a = "Personal Project"
# if "Miko" not in a:
#     print("Oh no no no thats not correct")