
# function
def medium():
    marks=[]
    multi_mark=[]
    print('Enter students marks : ')
    for i in range(5):
        read=int(input())
        marks.append(read)
    marks.sort(reverse=True)
    for i in marks:
        if i==marks[1]:
           multi_mark.append(i)
    if len(multi_mark)==1:
        return marks[1]
    else:
        return multi_mark
        
    #c=marks.count(marks[1])
    #if(c==1):
    #   print(marks[1])
    #else:
    #    print(marks[c])
m1=medium()
print('2nd position of student got : ',m1,' marks')


#class
class medium:
    def __init__(self,num):
        self.num=[]
        print('Enter marks : ')
        for i in range(5):
            read=int(input())
            self.num.append(read)
    def med(self):
        self.num.sort(reverse=True)
        return self.num[1]
m=medium(1)
medm=m.med()
print('2nd position of student got : ',medm)

