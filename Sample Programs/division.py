# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 12:41:07 2023

@author: DELL
"""

class Num:
    def __init__(self,num1):
        self.num1=num1
    def finddiv(self,num1,num2):
        self.num2=num2
        try:
           div=self.num1/self.num2
        except ArithmeticError:
            print('division by zero..please try again!!')
            self.num2=int(input())
            div=self.num1/self.num2
        return div
n1=int(input('Enter a number : '))
n2=int(input('Enter the divisor : '))
d=Num(n1)
print('Result : ',d.finddiv(n1,n2))