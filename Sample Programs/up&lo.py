# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 23:02:23 2023

@author: DELL
"""
#no of upper and lower cases in a string
def string(str):
    u=[]
    l=[]
    for i in str:
        if i.isupper():
            u.append(i)
        elif i.islower():
            l.append(i)
        else:
            pass
    return len(u),len(l)
str=input('Enter a string : ')
print('No: of upper and lowercases are : ',string(str))


