# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:39:06 2023

@author: DELL
"""

# 27 - leap year

yr=int(input("enter a year: "))
if((yr%400==0)or(yr%4==0 and yr%100!=0)):
    print('Leap year')
else:
    print('Not a Leap year')