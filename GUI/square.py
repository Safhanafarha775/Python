from tkinter import *
window=Tk()
window.title('Square')
window.geometry('400x450')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_inp=Label(frame,text='Click the button below to view square of numbers',font=20)
lbl_inp.grid(row=0,column=1)

def square():
    res='Number  || Square  \n'
    for i in range(1,11):
        res=res+'{0:^12}{1:^12}'.format(i,i**2)+'\n'
    lbl_res['text']=res

btn=Button(frame,text='Show',command=square,font=18)
btn.grid(row=1,column=1)

lbl_res=Label(frame,text='Number  || Square',font=15)
lbl_res.grid(row=3,column=1)

frame.grid(row=0,column=0)
window.mainloop()