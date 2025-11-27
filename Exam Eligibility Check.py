#Take input from studentthat he can attend exam or not
medical_cause=input("Did you have a medical cause Yes or No?: ")
#Take input of the students attendance
attendance=int(input("Enter the attendance of student(Percentage): "))

if medical_cause == 'Yes': #Checking first condition
    print("You are eligible")
else:
    if attendance >= 75: #Checking condition 2
        print("You are eligible")
    else:
        print("You are not eligible")