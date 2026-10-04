#When IGNORECASE is used, the text will be case insesitive.

# import re

# x = re.search('a+', 'aaaAAA') #This would only match the first three 'a's because the text is case sensitive.

# y = re.search('a+', 'aaaAAA', re.IGNORECASE) #This would match the entire string because the text is case insensitive.
# print(x)
# print(y)

#IGNORECASE isnt only used to find matches of the same letter,
#It can also be used to find matched of different letters, for example:
# x = re.search('[a-z]+', 'aBcDeF')
# y = re.search('[a-z]+', 'aBcDeF', re.I)
# print(x)
# print(y)