# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 10:56:00 2023

@author: DELL
"""


print('{0:15} {1:8} {2:6}'.format('Number','Square','Cube'))
for i in range(1,6):
    print('{0:<15} {1:<8} {2:<6}'.format(i,i**2,i**3))