# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 10:35:26 2023

@author: DELL
"""
#check whether a no is prime or not
n=int(input('Enter a number : '))
for i in range(2,n):
    if n%1!=0 and n%n!=0:
        pass
    else:
        return n
print(n,' is prime number')
