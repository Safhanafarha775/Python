# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:05:21 2023

@author: DELL
"""

##check whether the passed string is palindrome or not
def palindrome(s):
    rev=''
    l=len(str)
    while l>0:
        rev+=str[l-1]
        l=l-1
    if rev==str:
        return True
    else:
        return False    
str=input('Enter a string : ')
print('Is palindrome? : ',palindrome(str))
    
    