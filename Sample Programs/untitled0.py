# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:25:51 2023

@author: DELL
"""

lst=[]
s=0
print('Enter the numbes : ')
for i in range(0,6):
    n=int(input())
    lst.append(n)
for i in lst:
    s=s+i
print('Sum :',s)
