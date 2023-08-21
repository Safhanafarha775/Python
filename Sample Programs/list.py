# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 23:25:51 2023

@author: DELL
"""

# 15- program to print list

lst=[]
print('Enter the numbes : ')
for i in range(0,6):
    n=int(input())
    lst.append(n)
print('\nNumbers are : ')
for i in lst:
    print(i)
lst.clear()
print(lst)
