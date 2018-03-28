from tkinter import *

obj = Tk()

lbl = Label(obj,text = "Enter Name" )



lbl1 = Label(obj, text = "Enter ID")



e1 = Entry(obj)
e2 = Entry(obj,fg = "white")

lbl.grid(row =0)
lbl1.grid(row =1)

e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(obj, text = "SAVE")
b1.grid(row = 0, column = 2)

b2 = Button(obj, text = "SAVE")
b2.grid(row = 1, column = 2)

b3 = Button(obj, text = "RESET")
b3.grid(row =2)
obj.mainloop()

print("FINISHED")