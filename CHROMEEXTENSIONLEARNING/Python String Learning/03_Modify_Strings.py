#Upper Case
# The .upper() command returns the string in upper case letters

# Example:
# a = "personal project"
# print(a.upper())
#or
# print("personal project".upper())
#or
# print(a[0].upper() + a[1:8] + " " + a[9].upper() + a[10:])

#--------------------------------------------------------------------------------

#Lower Case
# The .lower() command returns the string in lower case letters

# a = "PERSONAL PROJECT"
# print(a.lower())
#OR
# print("PERSONAL PROJECT".lower())
#Or
# print(a[0] + a[1:8].lower() + " " + a[9] + a[10:16].lower())

#--------------------------------------------------------------------------------

#Remove Whitespace
#Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
#The .strip() method removes any whitespace from the beginning or the end:

# a = " Personal Project "
# print(a.strip())

#--------------------------------------------------------------------------------

#Replace String
#The .replace() method replaces a string with another string:
#Example
# a = "Personal Project"
# print(a.replace("Personal", "Miko"))

#--------------------------------------------------------------------------------

#Split Sring
#The .split() method splits the string into substrings if it finds instances of the separator:
#Example
# a = "Personal Project"
# print(a.split(" ")) #This will return ['Personal', 'Project']