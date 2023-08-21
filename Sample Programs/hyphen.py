# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:51:21 2023

@author: DELL
"""

#hyphen separated words in sorting order
str=input('Enter a string : ')
lst=str.split('-')
lst.sort()
print('-'.join(lst))
