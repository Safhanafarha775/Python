# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 23:16:37 2023

@author: DELL
"""

#program to get password and make sure that it contains alphabetics and numbers
pwd=input('Enter your password : ')
lst=[]
for i in pwd:
    if i.isalpha() or i.isnumeric():
        lst.append(True)
    else:
        lst.append(False)
def all(lst):
    for i in lst:
        if not i:
            print('Error..please try again')
    print('Passsword granted')
all(lst)


#or


class Details:
    def __init__(self,pwd):
        self.pwd=pwd
    def password(self,lst):
        self.lst=[]
        for i in self.pwd:
            if i.isalpha() or i.isnumeric():
                self.lst.append(True)
            else:
                self.lst.append(False)
    def all(self):
        for i in self.lst:
            if not i:
                 return False
        return True
pwd=input('Enter your password : ')
a=Details(pwd)
a.password(pwd)
a.all()