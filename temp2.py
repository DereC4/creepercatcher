from tkinter import * 
from tkinter import messagebox
import time
import tkinter
root = Tk()
root.geometry('471x687')
root.resizable(False, False)
root.title("Victory!!!")
root.geometry('852x480')
bg = PhotoImage(file = "assets/youwin.png")
B = tkinter.Button(root, text ="Hello")
B.pack()
frame1 = Frame(root)
frame1.pack(pady = 20 )

root.mainloop()