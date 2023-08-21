from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('Message Box')
window.geometry('400x400')


messagebox.showinfo('Info','Successfully completed')
messagebox.showwarning("Warning", "Warning")
messagebox.showerror("Error", "Error")
messagebox.askquestion("Question", "Are you sure?")
messagebox.askokcancel("Okcancel", "Want to continue?")
messagebox.askyesno("Yesno", "Are you sure?")
messagebox.askyesnocancel("Yesno", "Are you sure?")
messagebox.askretrycancel("Yesno", "Are you sure?")



window.mainloop()

