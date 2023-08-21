# 41-get an angle from the user and find sin and cos value
from math import sin
from math import cos
angle=float(input('enter an angle : '))
sres=sin(angle)
cres=cos(angle)
print('sin {} = '.format(angle),sres)
print('cos {} = '.format(angle),cres)


# 42-get number and find square,cube and sum of it
print('{0:15} {1:8} {2:6} {3:6}'.format('Number','Square','Cube','Sum'))
for i in range(1,6):
    print('{0:<15} {1:<8} {2:<6} {3:<6}'.format(i,i**2,i**3,i**2+i**3))


# 43-get starting and ending number and generate the sequence
start=int(input('Enter starting number : '))
end=int(input('Enter ending number : '))
print('Sequence : ')
for i in range(start,end+1):
    print(i)


# 44-get larger as starting and lower as ending and print it in reverse
start=int(input('Enter starting number : '))
end=int(input('Enter ending number : '))
num=[]
print('Sequence : ')
for i in range(start,end+1):
    num.append(i)
num.sort(reverse=True)
print(num)


# 45-print odd numbers between 1 to 30
print('Odd numbers between 1 and 30 are : ')
for i in range(0,31):
    if(i%2==1):
        print(i)


# 46-get mark of 5 subjects, store them into array and get students name, find total and print all


# 47-get 2 number ,find square and add both then display result
num=int(input('Enter a number : '))
sqr=num**2
print('Result = ',num+sqr)


# 48-get 2 number from user and display after swaping those numbers
num1=int(input('Enter 1st number : '))
num2=int(input('Enter 2nd number : '))
temp=num1
num1=num2
num2=temp
print('Numbers are {} and {} '.format(num1,num2))


# 49-program to get hours and convert into second
hour=int(input('Enter time in hours : '))
print('Time in seconds : ',hour*60*60)


# 50-program to find the area of triangle
base=int(input('Enter the base of traingle : '))
height=int(input('Enter the height of traingle : '))
print('Area of triangle : ',(base*height)/2)

