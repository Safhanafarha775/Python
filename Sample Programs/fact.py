# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:33:39 2023

@author: DELL
"""
#factorial of a number

n=int(input('Enter a number : '))
def factorial(x):
    fact=1
    for i in range(1,x+1):
            fact=fact*i
    return fact
print("Factorial= ",factorial(n))

    