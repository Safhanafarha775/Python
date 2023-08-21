from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Numbers')
window.geometry('400x450')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_inp=Label(frame,text='Enter numbers ',font=20)
lbl_inp.grid(row=0,column=0)
ent_inp=Entry(frame) 
ent_inp.grid(row=0,column=1)

def numbers():
    value=ent_inp.get()
    nums=value.split(',')
    res='Even Numbers \n-----------------\n'
    if len(nums)==5:
        for i in range(5):
            if int(nums[i])%2==0:
                res=res+nums[i]+'\n'
        lbl_res['text']=res
    else:
        messagebox.showwarning('Warning','Numbers should be exact 5 numbers')

btn_res=Button(frame,text='Submit',command=numbers)
btn_res.grid(row=1,column=2,sticky='w',padx=5)

lbl_res=Label(frame,text='')
lbl_res.grid(row=2,column=1)

frame.grid(row=0,column=0)
window.mainloop()