# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 00:03:07 2023

@author: DELL
"""

# 19- get 3 numbers and perform  a+b+ca/b(2a+2b)

print('Enter 3 numbers : ')
a=int(input())
b=int(input())
c=int(input())
res= (a+b+(c*a))/(b*(2*a+2*b))
print('Value of a+b+ca/b(2a+2b) = ',res)