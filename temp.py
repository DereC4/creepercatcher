from tkinter import * 
from tkinter import messagebox
import time

root = Tk()
root.geometry('720x1039')
root.title("Tic Tac Toe")
root.resizable(False, False)

bg = PhotoImage(file = "card.png")
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)
  
# Create Frame
frame1 = Frame(root)
frame1.pack(pady = 20 )
size = 20
count = 0
def byeButton():
    global size, count
    if(count<10):
        # print('hi')
        size -=2
        count += 1
        b1.config(font=("Helvetica",size))
        if(count<9):
            root.after(15,byeButton)
        else:
            b1.destroy()


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count, size
    clicked = True
    count = 0
    size = 20
    # Buttons
    b1 = Button(root, text = "Click me!", font=("Helvetica",20), activebackground='#12DEF5', height=40, width = 45, bg = "SystemButtonFace", command=lambda: byeButton())
    # b2 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b2))
    # b3 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b3))
    # b4 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b4))
    # b5 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b5))
    # b6 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b6))
    # b7 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b7))
    # b8 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b8))
    # b9 = Button(root, text = " ", font=("Helvetica",20), activebackground='#12DEF5', height=3, width = 100, bg = "SystemButtonFace", command=lambda: byeButton(b9))
    # # Grid
    b1.place(relx=0.5, rely=0.5, anchor=CENTER)
    # b2.place(x=0,y=120)
    # b3.place(x=0,y=240)
    # b4.place(x=0,y=360)
    # b5.place(x=0,y=480)
    # b6.place(x=0,y=600)
    # b7.place(x=0,y=720)
    # b8.place(x=0,y=840)
    # b9.place(x=0,y=960)

def exit():
    root.destroy()

mainMenu = Menu(root)
root.config(menu=mainMenu)
optionsMenu = Menu(mainMenu, tearoff= False)
mainMenu.add_cascade(label="Options", menu = optionsMenu)
optionsMenu.add_command(label="Restart Card", command = reset)
optionsMenu.add_command(label="Exit Card", command = exit)

reset()
root.mainloop()