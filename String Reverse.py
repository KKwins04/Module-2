#Input a word or a sentence
string = input("Please enter your own String: ")\

string2 = " "
#Loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe Original string: ", string)
print("The Reversed string: ", string2)