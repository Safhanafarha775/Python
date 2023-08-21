from tkinter import *
window=Tk()
window.title("Maximum/Minimum")
window.geometry('400x200')

frame=Frame(window)
lbl_num1=Label(frame,text='Enter 1st number :',width=35)
lbl_num1.grid(row=0,column=0)
lbl_num2=Label(frame,text='Enter 2nd number :',width=35)
lbl_num2.grid(row=1,column=0)

entry1=Entry(frame,width=10)
entry1.grid(row=0,column=1)
entry2=Entry(frame,width=10)
entry2.grid(row=1,column=1)
def maximum():
    num1=entry1.get()
    num2=entry2.get()
    if num1>num2:
        if int(num1)>0:
            lbl_res['text']='1st Number is Maximum and positive'
        else:
            lbl_res['text']='1st Number is Maximum and negative'
    elif num2>num1:
        if int(num2)>0:
            lbl_res['text']='2nd Number is Maximum and positive'
        else:
            lbl_res['text']='2nd Number is Maximum and negative'
    else:
        if num1.isnumeric() and num2.isnumeric():
            lbl_res['text']='both are same'
        else:
            lbl_res['text']="Entry of {}  {}".format(type(num1),type(num2))
        

btn=Button(frame,text='Result',command=maximum)
btn.grid(column=1,row=2)
lbl_res=Label(frame,text='',width=35)
lbl_res.grid(row=3,column=0)

frame.grid(row=0,column=0,padx=10)
window.mainloop()

