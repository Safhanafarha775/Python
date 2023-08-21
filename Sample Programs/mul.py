# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 10:58:15 2023

@author: DELL
"""

#multiplication of given numbers
from functools import reduce
n=[]
l=int(input('Enter the limit : '))
print('Enter numbers :')
for i in range(0,l):
    a=int(input())
    n.append(a)
reduce(lambda x,y: x+y,n)

n=[]

