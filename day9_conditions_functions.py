# Day 9 - Functions with Conditions

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is", check_even_odd(10))
print("7 is", check_even_odd(7))
num = int(input("Enter a number: "))
print(num, "is", check_even_odd(num))
