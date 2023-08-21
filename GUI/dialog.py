from tkinter import *
from tkinter import simpledialog
window=Tk()
window.title('Message Box')
window.geometry('400x400')
msg = simpledialog.askinteger("Input", "Input an Integer")
print(msg)
window.mainloop()
