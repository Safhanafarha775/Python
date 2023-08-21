# 91-find density of an object
mass=int(input('Enter mass of the object : '))
volume=int(input('Enter volume of the object : '))
print('Density = ',mass/volume)


# 92-find cieling of a number
import math
num = float(input("Enter a number : "))
print(math.ceil(num))


# 93-find acceleration of an object 
time=int(input('Enter time in seconds : '))
change_in_velocity=int(input('Enter change in velocity of object : '))
print('Acceleration = ',change_in_velocity/time)


# 94-force of a man on an object
mass=int(input('Enter mass of the object : '))
acceleration=int(input('Enter the acceleration of the object : '))
print('Force = ',mass*acceleration)


# 95-program to get the table of a number in reverse order
num = int(input("Enter a number : ")) 
for i in range(10,0,-1):
    print(num," * ",i," = ",num*i)


# 96-get 10 data from user and diffrentiate that into int,float,string etc 
lst = [1,3.3,'faisal','34','32',5.2,'age', 4,2,54]
int_type = []
float_type = []
string = []
for i in lst:
    if type(i)==int_type:
        int_type.append(i)
    if type(i)==float_type:
        float_type.append(i)
    if type(i)==str:
        string.append(i)
print("Integer Data type = "+str(int_type))
print("Floating Data Type = "+str(float_type))
print("String Data type = "+str(string))


# 97-get the middle element from the list of numbers 
num=[]
l=int(input('Enter length : '))
for i in range(l):
   read=int(input('Enter number : '))
   num.append(read)
s=(len(num)+1)/2
if type(len(num)/2)==int:
    print('No middle number existed')
else:
    print('Middle value of list is ',num[int(s)])


# 98-program to count prime number from 1-100
num=[]
for i in range(2,100):
    if i%1!=0 and i%i!=0:
        num.append(i)
    else:
        print(i,' is prime number')
        

# 99-program to get only uppercase letters
string=[]
upper=[]
for i in range(5):
    read=input('Enter word : ')
    string.append(read)
for i in string:
    if i.isupper():
        upper.append(i)
print('Uppercased words :  ',upper)

# 100-program to add number from list which is greater than 5 and less than 10
num=[]
num1=[]
for i in range(5):
    read=input('Enter number : ')
    num.append(read)
for i in num:
    if int(i)>5 and int(i)<10:
        num1.append(i)
print('Numbers greater than 5 and less than 10 are : ',num1)

# 101-display all student name except starts with 'f'
name=[]
for i in range(5):
    read=input('Enter name : ')
    name.append(read)
for i in name:
    if i[0]=='f':
        name.remove(i)
print('Names : ',name)

# 102-sort student name in ascending order and display which have 5 characters
std=[]
name=[]
print('Enter name of student : ')
for i in range(5):
    read=input()
    std.append(read)
for i in std:
    if len(i)==5:
        name.append(i)
print('Name which has 5 letters : ',name)