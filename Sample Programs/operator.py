# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 10:36:58 2023

@author: DELL
"""

# 24 - operator

a=int(input('first number : '))
b=int(input('second number : '))
opr=str(input('input the operator : '))
if(opr=='+'):
    print('sum = ',a+b)
elif (opr=='-'):
    print('difference = ',a-b)
elif(opr=='*'):
    print('product = ',a*b)
elif(opr=='/'):
    print('divison = ',a/b)
elif(opr=='%'):
    print('modulus = ',a%b) 
else:
    print('invalid operator')