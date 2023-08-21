import sys
from tkinter import *
from tkcalendar import *
from tkinter import ttk

window=Tk()
window.title('Flight Fare Prediction')
window.geometry('500x550')
window.resizable(width=False,height=False)
window.configure(bg='pink')

frame1=Frame(window,bg='white')
lbl_dep=Label(frame1,text='Dept Date',font=15,bg='white')
lbl_dep.grid(row=0,column=0,padx=10)
dept_date=StringVar()
cal1=DateEntry(frame1, width= 20, date_pattern="mm-dd-yyyy",textvariable=dept_date)
cal1.grid(row=1,column=0,padx=10)
lbl_deptime=Label(frame1,text='Dept Time',font=15,width=20,bg='white')
lbl_deptime.grid(row=0,column=1,padx=10)
dephour=IntVar()
sp1=Spinbox(frame1,from_=1,to=24,textvariable=dephour)
sp1.grid(row=1,column=1)
depmin=IntVar()
sp2=Spinbox(frame1,from_=00,to=59,)
sp2.grid(row=2,column=1)
frame1.place(x='70',y='80')

frame2=Frame(window,bg='white')
lbl_source=Label(frame2,text='Source',font=15,width=15,bg='white')
lbl_source.grid(row=0,column=0,padx=10)
source_data=StringVar()
combo1=ttk.Combobox(frame2,state='readonly',values=['Delhi','Kolkata','Banglore','Mumbai','Chennai '],textvariable=source_data)
combo1.grid(row=1,column=0)
lbl_dest=Label(frame2,text='Destination',font=15,width=20,bg='white')
lbl_dest.grid(row=0,column=1,padx=10)
dest_data=StringVar()
combo2=ttk.Combobox(frame2,state='readonly',values=['Cochin','Banglore','Delhi','New Delhi','Hyderabad','Kolkata'],textvariable=dest_data)
combo2.grid(row=1,column=1)
frame2.place(x='70',y='190')

frame3=Frame(window,bg='white')
lbl_stop=Label(frame3,text='Stopage',font=15,width=15,bg='white')
lbl_stop.grid(row=0,column=0,padx=10)
stop_data=IntVar()
combo3=ttk.Combobox(frame3,state='readonly',values=[0,1,2,3,4],textvariable=stop_data)
combo3.grid(row=1,column=0)
lbl_airline=Label(frame3,text='Airline',font=15,width=20,bg='white')
lbl_airline.grid(row=0,column=1,padx=10)
airline_data=StringVar()
combo4=ttk.Combobox(frame3,state='readonly',values=['Jet Airways','IndiGo','Air India','Multiple carriers','SpiceJet','Vistara','Air Asia','GoAir','Other'],textvariable=airline_data)
combo4.grid(row=1,column=1)
frame3.place(x='70',y='290')

button=Button(window,text='Submit',bg='light green')
button.place(x='220',y='380')

window.mainloop() 

