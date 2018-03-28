from tkinter import *

root = Tk()
root.title("CALCULATOR")
root.geometry("300x200+100+100")


def reset(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

def sum(event):

    num1 = v1.get()
    num2 = v2.get()

    SUM = num1 + num2
    e3.delete(0,END)
    e3.insert(0,SUM)

def minus(event):
    reset
    num1 = v1.get()
    num2 = v2.get()

    SUM = num1 - num2
    e3.delete(0, END)
    e3.insert(0,SUM)

def multi(event):
    num1 = v1.get()
    num2 = v2.get()

    SUM = num1 * num2
    e3.delete(0, END)
    e3.insert(0,SUM)

def division(event):
    num1 = v1.get()
    num2 = v2.get()

    SUM = num1 / num2
    e3.delete(0, END)
    e3.insert(0,SUM)

l1 = Label(root, text = "ENTER FIRST NO" ).grid(row = 0, sticky = W)
Label(root, text = "ENTER SECOND NO").grid(row = 1 , sticky = W)
Label(root, text = "RESULT").grid(row = 2 , sticky = W)

v1 = IntVar()
v2 = IntVar()

e1 = Entry(textvariable = v1)
e1.grid(row = 0, column = 1)
e2 = Entry(textvariable = v2)
e2.grid(row = 1, column = 1)

e3 = Entry()
e3.grid(row = 2, column = 1)

b1 = Button(text = "+", fg= "RED",padx = 15)
b1.grid(row = 4, column = 0,sticky = W)
b1.bind("<Button -1>",sum)

b2 = Button(text = "-", fg = "GREEN",padx = 15)
b2.grid(row = 5, column = 0,sticky = W)
b2.bind("<Button -1>",minus,reset)

b3 = Button(text = "*", fg = "BLUE",padx = 15)
b3.grid(row = 6, column = 0,sticky = W)
b3.bind("<Button -1>",multi)

b4 = Button(text = "%", fg = "CYAN",padx = 15)
b4.grid(row = 7, column = 0,sticky = W)
b4.bind("<Button -1>",division)

b5 = Button(text = "RESET")
b5.grid(row = 7, column = 1)
b5.bind("<Button -1>",reset)


root.mainloop()