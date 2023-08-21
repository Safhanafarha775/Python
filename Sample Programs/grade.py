# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:40:47 2023

@author: DELL
"""

# 31 - program to print grade

mark=int(input("Enter the mark : "))
if(mark>= 95):
    print("Grade = A+")
elif(mark>=80):
    print("Grade = A")
elif(mark>=70):
    print("Grade = B")
elif(mark>=60):
    print("Grade = C") 
else:
    print("Fail")