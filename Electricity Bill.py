#Take input of number of units consumed from the user
units = int(input("Enter the number of units consumed: "))

#Check conditions of units consumed
#Then calculate amount and subcharge accordingly
#Subcharge is the tax value

#Check for units less than 50
if(units < 50):
    amount = units * 2.60
    subcharge = 25

#Check for units less than 100
elif(units <= 100):
    amount = 130 + ((units - 50) * 3.25)
    subcharge = 35

#Check for units less than or equal to 200
elif(units <= 200):
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    subcharge = 45
# Check for all the cases other than mentioned
# When units consumed are more than 200
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    subcharge = 75

#Calculate and dispaly the total electricity bill
#Total amount = amount + subcharge
total = amount + subcharge
print("\nElectricity Bill = %.2f" %total)