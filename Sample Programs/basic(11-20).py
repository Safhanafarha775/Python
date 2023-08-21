#11- find maximum of 2 number
num1=int(input('Enter 1st number : '))
num2=int(input('Enter 2nd number : '))
if num1>num2:
    print('Maximum : ',num1)
else:
    print('Maximum : ',num2)

#12-star pyramid
n=6
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

# 13- get password from user (make sure that it contains alphabetics and numbers)
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

# 14- get six number in list and find sum
lst=[]
s=0
print('Enter the numbes : ')
for i in range(0,6):
    n=int(input())
    lst.append(n)
for i in lst:
    s=s+i
print('Sum :',s)

# 15- program to print list
lst=[]
print('Enter the numbes : ')
for i in range(0,6):
    n=int(input())
    lst.append(n)
print('\nNumbers are : ')
for i in lst:
    print(i)
lst.clear()
print(lst)


# 16- performing compund operators on a number
num=int(input('Enter a number : '))
num+=2
print(' Sum = ',num)
num-=2
print(' Diffrence = ',num)
num/=2
print(' Div = ',num)
num*=2
print(' Product  = ',num)


# 17- printing letters
print('A')
print('B \tC')
print('D \tE \tF')
print('G \tH \tI \tJ')
print('K \tL \tM')
print('N \tO')
print('P')


#18- store name and details in dictionary
details={}




# 19- get 3 numbers and perform  a+b+ca/b(2a+2b)
print('Enter 3 numbers : ')
a=int(input())
b=int(input())
c=int(input())
res= (a+b+(c*a))/(b*(2*a+2*b))
print('Value of a+b+ca/b(2a+2b) = ',res)


# 20- get 5 number in array then find sum of all

