# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:12:29 2023

@author: DELL
"""

age=int(input('Enter your age : '))
if age>18:
    print('You are eligible')
else:
    print('Sorry! you cannot participate in voting, you will be able to participate after {} years'.format(18-age))
