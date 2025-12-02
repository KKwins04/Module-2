base = float(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1
count = 0

while count < power:
    result = result * base
    count = count + 1

print("Result =", result)
