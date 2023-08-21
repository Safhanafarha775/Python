# 51-program to get days between two days
print('Enter 2 days :')
d1=int(input())
d2=int(input())
print('Number of days : ',d1-d2)


# 52-get a sentence and reverse
def string(s):
    rev=''
    l=len(s)
    n=list(range(0,l))
    n.sort(reverse=True)
    for i in n:
        rev=rev+s[i]
    return rev
str=input('Enter a string : ')
print(string(str)) 


# 53-get age in year and convert it into seconds
age=int(input('Enter your age in years : '))
res=age*365*24*60*60
print('Age in seconds : ',res)


# 54-find factorial of a number
n=int(input('Enter a number : '))
def factorial(x):
    fact=1
    for i in range(1,x+1):
            fact=fact*i
    return fact
print("Factorial= ",factorial(n)) 


# 55-show the current time of the user request


# 56-make a prcentage calculator
amount=int(input('Enter the amount : '))
per=int(input('Enter the percentage : '))
print('Amount = ',amount*20/100)


# 57-average calculator
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


# 58-get first and last name then display full name
first=input("Entr first name : ")
last=input("Entr last name : ")
print('Full Name : ',first+' '+last)


# 59-get bio from user and count characters and words in it
bio=input('Enter you bio : ')
words=bio.split(' ')
char=len(bio)
print('Number of characters : ',char)
print('Number od words : ',len(words))
    

# 60-get 5 author name and its book name then display the name of last author with his book
author= {}
for i in range(5):
    author_name = input("Enter author name ") 
    book_name = input("Enter its book name ")
    author[author_name] = book_name

print("Last author is ",list(author.keys()[-1]))
print("Last book is ",list(author.values()[-1]))

