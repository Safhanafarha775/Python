class Number:
    def __init__(self,num):
        self.num=num
    def sum(self):
        res=0
        for i in self.num:
            res=res+i
        return res
            
lst=[]
len=int(input('enter limit'))
print('Enter numbers :')
for i in range(0,len):
    while True:
        try:
            n=int(input())
        except ValueError:
            print('Invalid input..Please try again!!!')
            continue
            #n=int(input())
        else:
            break
        #finally:
            #print('Value accepted')
    lst.append(n)
s=Number(lst)
print('Sum = ',s.sum())

