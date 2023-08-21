from tkinter import *
window=Tk()
window.title('Username')
window.geometry('400x450')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_inp=Label(frame,text='Enter Username ',font=20)
lbl_inp.grid(row=0,column=0)
ent_inp=Entry(frame) 
ent_inp.grid(row=0,column=1)

       
def letters():
    value=ent_inp.get()
    if value.isalnum():
        lbl_res['text']='Username accepted'
    else:
        messagebox.showwarning('Warning','Username should be Alphanumberic')
    

btn_res=Button(frame,text='Submit',command=letters)
btn_res.grid(row=1,column=2,sticky='w',padx=5)

lbl_res=Label(frame,text='')
lbl_res.grid(row=2,column=1)

frame.grid(row=0,column=0)
window.mainloop()
