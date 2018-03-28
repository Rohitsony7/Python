from tkinter import *

obj = Tk()

lbl = Label(obj,text = "Demo for the lable", bg = "yellow", fg = "black")

lbl.pack(fill = X)

lbl1 = Label(obj, text = " Welcome to the future",fg = "black", bg = "blue")

lbl1.pack(fill = X)

e1 = Entry(obj)
e2 = Entry(obj)



obj.mainloop()

print("Finished")



