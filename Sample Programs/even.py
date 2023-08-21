# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 20:30:47 2023

@author: DELL
"""

#function to print even numbers of a list
def even(n):
    e=[]
    for i in n:
        if i%2==0:
            e.append(n)
        else:
            pass
lst=(2,3,4,7,8,4,6)
print('Even numbers are : ',even(lst))

n=int(input('Enter limit: '))
lst=[]
print('Enter elements : ')
for i in range(0,n):
    s=input()
    lst.append(s)
print('List :',lst)
