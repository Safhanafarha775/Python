# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 22:39:05 2023

@author: DELL
"""

#program to get 6 subject marks and find total and average
m=[]
total=0
print('Enter mark of six subjects : ')
for i in range(0,6):
    mark=int(input())
    m.append(mark)
for i in m:
    total=total+i
print('Total = ',total)
print('Average = ',total/6)