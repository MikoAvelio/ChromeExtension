#re.search(<regex>, <string>) scans <string> looking for the first location where the pattern <regex> matches. If a match is found, then re.search() returns a match object. 
#if nothing is found, it returns None.
#to use re.search(), you need to import the re module first. Then, you can call the re.search()

#Examples of importing:
# import re
# re.search(...)
#or
# from re import search
# search(...)

#Re.search Matching Example:
import re
txt = "My Personal Project"

#Check if the string contains "Personal":
x = re.search("Personal", txt)

if x is not None:
  print(txt + " contains the word 'Personal'")

if x is None:
  print("No match")