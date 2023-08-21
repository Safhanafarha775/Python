from tkinter import *
window=Tk()
window.title('Counting')
window.geometry('400x300')
window.resizable(width=False,height=False)

frame=Frame(window)
lbl_str=Label(frame,text='Enter your string ',width=20)
lbl_str.grid(row=0,column=0)
ent_str=Entry(frame,width=30)
ent_str.grid(row=0,column=1)

def string():
    string=ent_str.get()
    ch=string.split(' ')
    wrd=len(ch)
    space=wrd-1
    char=len(string)
    lbl_words['text']='Number of words : {}'.format(wrd)
    lbl_spaces['text']='Number of spaces : {}'.format(space)
    lbl_char['text']='Number of characters : {}'.format(char)
    
btn_show=Button(frame,text='Show',command=string)
btn_show.grid(row=1,column=1)
    
frame1=Frame(window)
lbl_words=Label(frame1,text='Number of words : ')
lbl_words.grid(row=0,column=0,sticky='w')
lbl_spaces=Label(frame1,text='Number of spaces : ')
lbl_spaces.grid(row=1,column=0,sticky='w')
lbl_char=Label(frame1,text='Number of characters : ')
lbl_char.grid(row=2,column=0,sticky='w')

frame.grid(row=0,column=0)
frame1.grid(row=1,column=0)
window.mainloop()