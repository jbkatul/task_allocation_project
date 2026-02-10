from django.shortcuts import render

# Create your views here.

# feature multiplication of two number 

def multiply(a, b):
    return a * b


result = multiply(5, 3)
print(result)  

def divison(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"
result = divison(10, 2)
print(result)

def subtraction(a, b):
    return a - b    
result = subtraction(10, 5)
print(result)

print("end of the code")
