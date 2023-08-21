# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:38:07 2023

@author: DELL
"""

#function that takes a list a return a new list with unique elements of first list
def list(l):
    return(set(l))
n=int(input('Enter limit: '))
lst=[]
print('Enter elements : ')
for i in range(0,n):
    s=input()
    lst.append(s)
print('Unique elements are : ',list(lst))
