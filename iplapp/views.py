from django.shortcuts import render

# Create your views here.
# this is Dev 1 -> Atul sir's feature

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)