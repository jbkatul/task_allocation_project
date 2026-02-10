from functools import reduce
from django.shortcuts import render

# Create your views here.
# This is Saiprasad => 

def MaxNumber(ls):
    return reduce(lambda x,y: x if x>y else y, ls)
 