from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Colours')
window.geometry('400x450')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_inp=Label(frame,text='Enter colours ',font=20)
lbl_inp.grid(row=0,column=0)
ent_inp=Entry(frame) 
ent_inp.grid(row=0,column=1)

def colours():
    value=ent_inp.get()
    clrs=value.split(',')
    res='Colours     || Characters \n------------------------------\n'
    if len(clrs)==5:
        for i in clrs:
            res=res+'{0:<10}{1:^16}'.format(i,len(i))+'\n'
        lbl_res['text']=res
    else:
        messagebox.showwarning('Warning','Colours should be exact 5 numbers')

btn_res=Button(frame,text='Submit',command=colours)
btn_res.grid(row=1,column=2,sticky='w',padx=5)

lbl_res=Label(frame,text='Colours     || Characters ')
lbl_res.grid(row=2,column=1)

frame.grid(row=0,column=0)
window.mainloop()