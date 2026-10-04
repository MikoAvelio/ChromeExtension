#Slicing:
#You can return a range of chractures by using the slice syntax.
#Specify the start and the end by stating the nnumber of the assigned chracterm then seperate them with a colon.

#Example: 
# a = "Personal Project"
# print(a[3:8]) #This will return the characters from position 3 to position 6.
# print(a[0:16:2]) #The third parameter is the step, a step tells the code to skip a number of characters in the string. In this case, it will return every second character from position 0 to position 15.

#--------------------------------------------------------------------------------

#Slicing From the Start:
#By leaving out the start parameter, the range will start at the first character:
# Example:
# a = "Personal Project"
# print(a[:8]) #This will return the characters from position 0 to position 7

#--------------------------------------------------------------------------------

#Slicing To the End:
#By leaving out the end parameter, the range will go to the end of the string:

# Example:
# a = "Personal Project"
# print(a[3:]) #This will return the characters from position 3 to the end of the string.

#--------------------------------------------------------------------------------

#Negative Indexing:
#Use negative indexes to start the slice from the end of the string:
# Example:
# a = "Personal Project"
# print(a[-5:-2])
