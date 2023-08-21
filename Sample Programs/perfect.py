# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:47:42 2023

@author: DELL
"""

#check whether the function is perfect or not
def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum=sum+i
        else:
            pass
    return sum==n
Num=int(input('Enter a number : '))
print(perfect(Num))