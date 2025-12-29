# EVEN / ODD
num = int(input("Enter a number: ").strip())

if num % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")


# POSITIVE / NEGATIVE / ZERO
num2 = int(input("Enter another number: ").strip())

if num2 > 0:
    print("Positive number")
elif num2 < 0:
    print("Negative number")
else:
    print("Number is zero")


# NUMBERS FROM 1 TO 10
print("Numbers from 1 to 10:")
for i in range(1, 11):
    print(i)
