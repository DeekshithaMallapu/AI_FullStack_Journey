# DAY 5: Function in python
def greet():
    print("Hello, Welcome to Day 5!")
greet()
def add(a,b):
    return a + b
result=add(5,3)
print("sum is:",result)

def check_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
print(check_even(7))
