import re

data = "My Personal Project" #Just an example string later on it will be pulled from my JSON file.

user_query = input("Enter a keyword(s): ")
advanced_search = input("Do you want to use advanced search? (Yes/No): ").lower() == "yes" #This will also be connected to my frontend later on

if not advanced_search:
  search = re.escape(user_query)
else:
  search = user_query

match_result = re.search(search, data, re.IGNORECASE)
if match_result:
  print(f"Match found: {match_result.group()}")
else:
  print("No match found.")