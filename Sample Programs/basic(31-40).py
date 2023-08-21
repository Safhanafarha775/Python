# 31 - program to check grade
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


# 32-find maximum of two numbers using function
n1=int(input('Two numbers : '))
n2=int(input())
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
maximum(n1,n2)


# 33- get the number colours in a list
color=['pink','red','green','white','black']
print('no of color in the list = ',len(color))


# 34- get 5 colours in a list and remove last colour from a list and print
color=[]
for i in range(0,5):
    color.append(input('enter the color : '))
print(color) 
color.pop(4)
print(color)


# 35- get 10 name of students and print in descending order
stud=[]
print('Enter the name of students : ')
for i in range(0,10):
    name=input()
    stud.append(name)
stud.sort(reverse=True)
print(stud)


# 36- program to capitalise a sentence
a=input('write a sentence : ')
#print(a.upper())
print(a.capitalize())


# 37- find cube of a number
n=int(input('enter a number : '))
print('cube = ',n*n*n)


# 38-find degreeof a radian

from math import pi
radian=int(input('enter the radian'))
degree=radian*180/pi
print(degree)

#or
import math
r = int(input("Enter the radian"))
d= math.degrees(r)
print(d)


# 39- find sum and product of all elements in a list
lst=[]
for i in range(0,4):
    lst.append(int(input('enter the no : ')))
def arithop(num):
    add=0
    mul=1
    for i in num:
        add=add+i
        mul=mul*i
    print('sum =',add)
    print('product =',mul)
arithop(lst)


# 40-getting username from the user
uname=input('UserName : ')
def username(a):
    if a.isalnum():
        return('your username is {}'.format(uname))
    else:
         return('wrong username')  
username(uname)

