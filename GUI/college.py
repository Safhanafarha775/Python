from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
base=Tk()
base.geometry('800x5500')
base.title('College Admission Form')

cTableContainer = Canvas(base)
fTable = Frame(cTableContainer)
sbHorizontalScrollBar = Scrollbar(base)
sbVerticalScrollBar = Scrollbar(base)

def createScrollableContainer():
	cTableContainer.config(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar.set, highlightthickness=0)
	sbHorizontalScrollBar.config(orient=HORIZONTAL, command=cTableContainer.xview)
	sbVerticalScrollBar.config(orient=VERTICAL, command=cTableContainer.yview)

	sbHorizontalScrollBar.pack(fill=X, side=BOTTOM, expand=FALSE)
	sbVerticalScrollBar.pack(fill=Y, side=RIGHT, expand=FALSE)
	cTableContainer.pack(fill=BOTH, side=LEFT, expand=TRUE)
	cTableContainer.create_window(0, 0, window=fTable, anchor=NW)
def updateScrollRegion():
	cTableContainer.update_idletasks()
	cTableContainer.config(scrollregion=fTable.bbox())

createScrollableContainer()
updateScrollRegion()

base.after(1000)

#sb=Scrollbar(base,orient='vertical')
#sb.pack(side=RIGHT,fill=Y)
#sb.config(command=sb.set)

lab0=Label(base, text='COLLEGE ADMISSION FORM ', width=25, font=('bold',25))
lab0.place(x=10,y=25)
lab1=Label(base, text='Enter your admission information below', width=30, font=8)
lab1.place(x=17,y=65)

lab2=Label(base, text='Name', width=5, font=('bold',15))
lab2.place(x=18,y=130)
entry1=Entry(base, width=15, font=('bold',20))
entry1.place(x=25,y=180)
entry2=Entry(base, width=15, font=('bold',20))
entry2.place(x=280,y=180)
entry3=Entry(base, width=15, font=('bold',20))
entry3.place(x=540,y=180)
lab3=Label(base, text='First Name', width=12, font=('bold',10))
lab3.place(x=10,y=220)
lab4=Label(base, text='Middle Initial', width=12, font=('bold',10))
lab4.place(x=270,y=220)
lab5=Label(base, text='Last Name', width=12, font=('bold',10))
lab5.place(x=530,y=220)

lab6=Label(base, text='Birth Date', width=10, font=('bold',15))
lab6.place(x=13,y=270)
date=DateEntry(base, width=10)
date.place(x=28,y=310)
entry10=Entry(base, width=15, font=('bold',20))
entry10.place(x=25,y=180)
entry11=Entry(base, width=15, font=('bold',20))
entry11.place(x=280,y=180)
entry12=Entry(base, width=15, font=('bold',20))
entry12.place(x=540,y=180)


lab7=Label(base, text='Gender', width=10, font=('bold',15)).place(x=5,y=350)
gen=IntVar()
Radiobutton(base, text='Male',variable=gen,value=1,font=(12)).place(x=28,y=380)
Radiobutton(base, text='Female',variable=gen,value=2,font=(12)).place(x=100,y=380)

lab8=Label(base, text='Of which country are you a citizen?', width=30, font=('bold',15))
lab8.place(x=400,y=350)

menu= StringVar()
menu.set("Select state ")
import pandas as pd
df=pd.read_csv("C:\\Users\\DELL\\Documents\\countries.csv")
df=df['name']
countrylist=list(df)
lst=OptionMenu(base,menu,*countrylist)
lst.place(x=430,y=380)

lab9=Label(base, text='Phone',width=7,font=('bold',15))
lab9.place(x=15,y=430)
def temp_text(e):
    entry4.delete(0,"end")
entry4=Entry(base, width=22, font=('bold',20))
entry4.place(x=28,y=460)
entry4.insert(0, "(000) 000-0000")
entry4.bind("<FocusIn>", temp_text) 
#entry4.wm_attributes()

lab10=Label(base, text='Email',width=7,font=('bold',15))
lab10.place(x=400,y=430)
entry5=Entry(base,width=22, font=('bold',20))
entry5.place(x=419,y=460)
lab11=Label(base, text='example@example.com',width=20,font=('bold',8))
lab11.place(x=420,y=500)

lab12=Label(base, text='Mailing Address',width=16,font=('bold',15))
lab12.place(x=9,y=520)
entry6=Entry(base,width=49, font=('bold',20))
entry6.place(x=28,y=560)
lab13=Label(base, text='Street Address',width=15,font=('bold',8))
lab13.place(x=17,y=600)
entry7=Entry(base,width=49, font=('bold',20))
entry7.place(x=28,y=630)
lab14=Label(base, text='Street Address Line2',width=20,font=('bold',8))
lab14.place(x=17,y=670)
entry8=Entry(base,width=22, font=('bold',20))
entry8.place(x=28,y=690)
lab15=Label(base, text='City',width=5,font=('bold',8))
lab15.place(x=15,y=720)
entry9=Entry(base,width=22, font=('bold',20))
entry9.place(x=419,y=690)
#lab16=Label(base, text='State/Province',width=15,font=('bold',8))
#lab16.place(x=420,y=730)
#entry10=Entry(base,width=49, font=('bold',20))
#entry10.place(x=28,y=750)
#lab17=Label(base, text='Postal/Zip code',width=15,font=('bold',8))
#lab17.place(x=15,y=800)

base.mainloop()