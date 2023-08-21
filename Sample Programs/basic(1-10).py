# 1-square and cube of number
print('{0:15} {1:8} {2:6}'.format('Number','Square','Cube'))
for i in range(1,6):
    print('{0:<15} {1:<8} {2:<6}'.format(i,i**2,i**3))

# 2-area of circle and rectangle
from math import pi
r=int(input('Enter radius: '))
print('Area of circle = ',pi*r*r)


l=int(input('Enter length: '))
b=int(input('Enter breadth: '))
print('Area of rectangle= ',l*b)

# 3-print name and address
name=input('Enter name: ')
age=int(input('Enter age: '))
print('Hi {}! Your age is {}'.format(name,age))

addrs=input('Enter your address : ')
mark=int(input('Enter your marks: '))
print('Your address is "{}" and your marks is "{}"'.format(addrs,mark))

# 4-voting age
age=int(input('Enter your age : '))
if age>18:
    print('You are eligible')
else:
    print('Sorry! you cannot participate in voting, you will be able to participate after {} years'.format(18-age))

# 5- arithmetic operators
x=int(input('Enter first number : '))
y=int(input('Enter second number : '))
print('Sum= ',x+y)
print('Difference= ',x-y)
print('Product= ',x*y)
print('Division= ',x/y)
print('Modulus=',x%y)

# 6,7,8-set operations (program to find union, intersection and diffrence of 2 sets)

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

# 9-program to get number from the user and display table for that number
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


# 10-program to get 6 subject marks and find total and average
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



