# -*- coding: utf-8 -*-
"""
C{reated on Thu Feb  2 23:34:45 2023

@author: DELL
"""

#program to find union, intersection and diffrence of 2 sets

a={2,3,8}
b={4,8,0}
c={2,7,9}
print('Union : ',a.union(b.union(c)))
print('Intersection : ',a.intersection(b.union(c)))
print('Diffrence : ',a.difference(b))
#or

def values():
    l=int(input('Enter a limit : '))
    a=[]
    print('Enter the numbers ')
    for i in range(0,l):
        n=int(input())
        a.append(n)
    return a
print('Creating first set...')
x=set(values())
print('Creating second set...')
y=set(values())
print('Union of sets : ',x.union(y))
print('Intersection of sets : ',x.intersection(y))
print('Diffrence of sets : ',x.difference(y))

