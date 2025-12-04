# Convert decimal (including fractions) to binary using loops 

num = float(input("Enter a decimal number: "))

#Split into integer and fractional parts
integer_part = int(num)
fraction_part = num - integer_part

# Convert integer part using loops
binary_int = ""

if integer_part == 0:
    binary_int = "0"
else:
    n = integer_part
    while n > 0:
        remainder = n % 2
        # prepend remainder
        binary_int = str(remainder) + binary_int
        n = n // 2

#Convert fractional part using loops 
binary_frac = ""
f = fraction_part
count = 0       # prevents infinite repeating fractions

while f > 0 and count < 20:
    f = f * 2
    bit = int(f)   # will be 0 or 1
    binary_frac = binary_frac + str(bit)
    f = f - bit
    count = count + 1

#Final Output
if binary_frac == "":
    print("Binary:", binary_int)
else:
    print("Binary:", binary_int + "." + binary_frac)
