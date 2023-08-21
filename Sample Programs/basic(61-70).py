# 61-convert GB into bytes
gb  = float(input("Enter memory in GB : ")) 
byte= 1073741824 * gb
print("GB is converted to Bytes : ",byte)


# 62-print detaisl of student in following format
name = input("Enter your full name : ")
f_name = input("Enter your father  name : ")
cnic = input("Enter your CNIC : ")
age = input("Enter your age : ")
contact = input("Enter your contact : ")

print("This is a student informaiton that we get from user")
print("{0:12} {1:15}".format('Name ',name))
print("{0:12} {1:15}".format('Father Name ',f_name))
print("{0:12} {1:15}".format('CNIC ',cnic))
print("{0:12} {1:15}".format('Age',age))
print("{0:12} {1:15}".format('Contact ',contact))


# 63-maximum of numbers in list
lst = []
print('Enter numbers : ')
for i in range(10):
    lst.append(int(input()))

def max_num(l):
    print(max(l))
max_num(lst)


# 64-student admission scholarship based on grade
mark = int(input("Enter your marks"))
if(mark == 1100):
    print("Free Education")
elif (mark > 1000):
    print("80%  Monthly Fees Deduction")
elif (mark > 900):
    print("60%  Monthly Fees Deduction")
elif (mark > 800):
    print("40%  Monthly Fees Deduction")
elif (mark > 700):
    print("30%  Monthly Fees Deduction")  
elif (mark > 600):
    print("There Is No Scholarship")
else:
    print("Enter valid number!!")


# 65-area and perimeter of square
l = float(input("Enter lenght of square : "))
def area_peri(length):
    area = length*length
    perimeter = 4*length
    print("Area = ",area)
    print("Perimeter = ",perimeter)
area_peri(l)


# 66-

# 67-sum of two numbers
num1 = int(input("Enter 1st num"))
num2 = int(input("Enter 2nd num"))

if((num1>0 and num2>0) and (num1<50 and num2<50)):
    print("Addition of both number : ",num1+num2)
else:
    print("Number should be positive and less than 50")
    
    
# 68-accpets 6 identity number and display in descending order
std_id = []
print('Enter student id : ')
for i in range(6): 
    std_id.append(int(input()))
std_id.sort(reverse = True)
print(std_id)


# 69-open a file and write username and age
file=open('Details.txt','w+')
name=input('Enter your name : ')
age=input('Enter your age : ')
file.write('Name : '+str(name))
file.write('Age : '+str(age))
file.close()
    
    
# 70-find duplication of student id
std_id=[]
for i in range(0,10):
    id=int(input('Enter id : '))
    std_id.append(id)
#print(std_id)
ids=set(std_id)
if len(ids)==len(std_id):
    print('No id is duplicated')
else:
    print('id of students after removing duplicated ones : ',ids)
    
    
