#Input a number
num = int(input("Enter the number: "))
t = num
numLen = 0

#Iterate the loop
while t>0:
    numLen = numLen + 1
    t = int(t/10)

if numLen >= 4: #Condition 1
    numLen = int(numLen/2)
    chk = 0
    while num > 0: #Iterate loop 1
        rem = num % 10
        if chk==numLen: #Nested loop 1
            midOne = rem
        elif chk == (numLen-1):
            midTwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midOne*midTwo #Product ofmiddle digits
    #Display the result
    print("\nProduct of middle digits (" +str(midOne)+ "*" +str(midTwo)+ ") = ",prod)

else:
    print('\nIt is not a 4 or more than 4-digit number!')