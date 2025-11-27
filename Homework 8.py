# Get age input from the user
age = int(input("Enter your age: "))

# Nested if statements to check age
if age >= 10:
    if age <= 20:
        print("You are eligible to enroll in the program.")
    else:
        print("Sorry, you are older than the allowed age for enrollment.")
else:
    print("Sorry, you are younger than the allowed age for enrollment.")
