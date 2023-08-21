# 21- get 5 number in array then find maximum


# 22-program to check vowel or not
l=input('enter the letter : ')
l=l.lower()
if l in ('a','e','i','o','u'):
    print('vowel')
else:
    print('consonant')
    

# 23 -  to check the day holiday or not                                                                                                                                 
n=input('enter the day : ')
if (n.upper()=='SUNDAY'):
    print('holiday')
else:
    print('not holiday')


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

# 25 - mark pass
mark= int(input("Enter the Mark : "))

if(mark>= 40):
    print(" Pass")
else:
    print(" Fail")

    
# 26- check the number is even or odd
n=int(input("Enter the number : "))
if (n%2 == 0):
    print("even number")
else:
    print("odd number")

    
# 27 - leap year
yr=int(input("enter a year: "))
if((yr%400==0)or(yr%4==0 and yr%100!=0)):
    print('Leap year')
else:
    print('Not a Leap year')
    

# 28- to find square
n = int(input("Enter a number : "))
sqr = n*n
print("Square = ",sqr)


# 29 - program to check positive or not 
n=int(input("Enter a number : "))
if(n>0):
    print("Positive Number")
else:
    print("Negative Number")


# 30- divisible by 2 and 3
n=int(input("Enter a number : "))
if(n%2==0 and n%3==0):
    print("Number is divisbile by 2 & 3")
else:
    print("Not divisible by 2 & 3")