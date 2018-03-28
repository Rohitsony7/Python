from tkinter import *

from asyncio import events

root = Tk()
root.title("Demo of GUI in pytthon")

l1 = Label(text = 'Name')
l2 = Label(text = 'User_ID')
l1.place(x=10 , y = 10)
l2.place(x= 10, y = 40)

e1 = Entry()
e2 = Entry()
e1.place(x=60, y =10)

def left(event):
    print("LEFT BUTTON is clicked")

def right(event):
    print("RIGHT BUTTON is clicked")

def middle(event):
    print("MIDDLE BUTTON is clicked")

def cmnd():
    print("Event hadling by command")

e2.place(x =60, y =40)
b1 = Button(text = "SAVE", bg = "YELLOW", COMMAND = cmnd()) # Event handling by command
b1.place(x = 10, y = 70)
b1.bind('<Button-1>',left)   # event handling by binding
b1.bind('<Button-2>',middle) # event handling by binding
b1.bind('<Button-3>', right) # event handling by binding



root.mainloop()


