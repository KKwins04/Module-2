#Take input of a string
str1 = input("Please enter a sentence: ")
total = 1 #initialise

for i in range(len(str1)):
#loop will runto calculate the length using string operation
    if(str1[i] == ' '):
#condition 1
        total = total + 1

print("Total number of words in this string is: ", total)