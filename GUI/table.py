from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Multiplication Table')
window.geometry('600x400')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_inp=Label(frame,text='Enter a number ',width=20,font=18)
lbl_inp.grid(row=0,column=0)
ent_num=Entry(frame,width=20,font=18)
ent_num.grid(row=0,column=3)

def table():
    num=int(ent_num.get())
    str1='Table of '+str(num)+'\n----------------\n'
    for i in range(1,11):
        str1=str1+" "+'{} x {} = {}'.format(num,i,num*i)+"\n"
    lbl_res.configure(text=str1,justify=LEFT)
    #lbl_res['text']=str1

btn=Button(frame,text='Show table',command=table,font=18)
btn.grid(row=1,column=3)
frame1=Frame(window)
lbl_res=Label(frame1,text='',font=15)
#lbl_res=Label(frame1,text='',font=15,justify=LEFT)
lbl_res.grid(row=3,column=2)

#messagebox.showinfo('success','Successfully completed')
#messagebox.askquestion("askquestion", "Are you sure?")

frame.grid(row=0,column=0)
frame1.grid(row=1,column=0)
window.mainloop()
