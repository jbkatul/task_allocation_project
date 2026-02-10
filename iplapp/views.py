from django.shortcuts import render

# Create your views here.
# by Renuka Patil

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

print("End")
print("coding")



def is_palindrome(s):
    return s == s[::-1]
