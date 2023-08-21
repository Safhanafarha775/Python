# 71-program to count of a specific word or sentence
sen=input('Enter a sentence : ')
search=input('Enter the word or character to search : ')
print('Number of word or character in sentence is : ',sen.count(search)

      
# 72-shuffle the list of color code
import random
colour=[]
print('Enter colour codes : ')
for i in range(5):
    read=input()
    colour.append(read)
print('colour codes : ',colour)
random.shuffle(colour)
print('Shuffled list of colour codes : ',colour)
    

# 73-get sentence from user , get last character of sentence and display,and display all characters
sen=input('Enter a sentence : ')
print('Last character of sentence is ',sen[-1])
print('Letters in sentence are : ')
for i in sen:
    print(i)


# 74-get student mark and display 2nd position of student
marks=[]
print('Enter students marks : ')
for i in range(5):
    read=int(input())
    marks.append(read)
marks.sort(reverse=True)
print('2nd position of student got : ',marks[1],' marks')


# 75-clone or copy the color list
colour=[]
print('Enter colours  : ')
for i in range(5):
    read=input()
    colour.append(read)
copy_colour=colour.copy()
print('List of colours : ',colour)
print('Cloned colour list : ',copy_colour)


# 76-display number which is divisible by 3 from a list
num=[]
for i in range(10):
    read=input('Enter number : ')
    num.append(read)
print('Numbers divisible by 3 are : ')
for i in num:
    if i%3==0:
        print(i)

# 77-check the first and last number of tuple is same or not 
num=(1,2,3,4,5,3)
if num[0]==num[-1]:
    print('First and last number are same')
else:
    print('First and last number are not same')
    

# 78-get a number and return its previous number along with that number
num=int(input('Enter a number : '))
print('Num is {} and previous number is {}'.format(num,num-1))


# 79-print first and last characters of sentence
sen=input('Enter a sentence : ')
print('First character is {} and last is {}'.format(sen[0],sen[-1]))

# 80-print characters of a sentence that are of odd index number
sen=input('Enter a sentence : ')
for i in range(len(sen)):
    if i%2==1:
        print(sen[i])

