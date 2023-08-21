# 81-program to find sum of first and last number of a list
num=[]
for i in range(10):
    read=input('Enter number : ')
    num.append(read)
print('Sum of first and last number : ',int(num[0])+int(num[-1]))


# 82-

# 83-get name starts with 'f' from a list of names
name=[]
for i in range(5):
    read=input('Enter name : ')
    name.append(read)
print('Name start with "f" are : ')
for i in name:
    if i[0]=='f':
        print(i)
        

# 84-get name from user, then check if it is in uppercase or not and convert if not
name=input("Enter your name : ")
if name.isupper():
    print('Name is in uppercase.')
else:
    print(name.upper())


# 85-get name that ends with 'n' from a list of names 
name=[]
for i in range(5):
    read=input('Enter name : ')
    name.append(read)
print('Name end with "n" are : ')
for i in name:
    if i[-1]=='n':
        print(i)


# 86-

# 87-get a sentence from user and display only 10 charcters
sen=input('Enter a sentence : ')
for i in range(len(sen)):
    if i<10:
        print(sen[i],end='')


# 88-get a number and display after adding the half of that number into it
num=int(input('Enter a number : '))
print('Result : ',num+num/2)


# 89-generate set of odd and even numbers separately from 0-20 and display by joining it 
even=[]
odd=[]
for i in range(0,20):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
#print('set of even numbers : ',even)
#print('set of odd numbers : ',odd)
s1=set(even)
s2=set(odd)
s1.union(s2)


# 90-get list of age of students from user and display the age which is greater than 14 and less than 20 
age=[]
for i in range(10):
    read=int(input('Enter age : '))
    age.append(read)
print('Age between 14 and 20 : ')
for i in age:
    if int(i)>14 and int(i)<20:
        print(i)
