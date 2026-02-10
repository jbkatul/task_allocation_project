from django.shortcuts import render

# Create your views here.
# by harshada

def even_no(addtion):
    if addition % 2 == 0:
        return "Even"
    else:
        return "Odd"

