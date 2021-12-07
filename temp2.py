from tkinter import * 
from tkinter import messagebox
import time

root = Tk()
root.geometry('471x687')
root.title("Happy Birthday Mom!")
root.resizable(False, False)

bg = PhotoImage(file = "assets/momcard.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )
size = 20    


root.mainloop()