# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:00:39 2023

@author: DELL
"""
#program to find reverse of a string
def string(s):
    rev=''
    l=len(s)
    while l>0:
        rev=rev+s[l-1]
        l=l-1
    return rev
str=input('Enter a string : ')
print(string(str))
    
    
def string(s):
    rev=''
    l=len(s)
    n=list(range(0,l))
    n.sort(reverse=True)
    for i in n:
        rev=rev+s[i]
    return rev
str=input('Enter a string : ')
print(string(str))  