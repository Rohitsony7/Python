from tkinter import *

root = Tk()

root.title("DEMO OF INSERT AND DELETE")
root.geometry("300x120+100+100")

Label(root, text= "FIRST NAME").grid(row = 0 , sticky = W)
Label(root, text= "LAST NAME").grid(row = 1 , sticky = W)
Label(root, text= "MOBILE NO").grid(row = 2 , sticky = W)
Label(root, text= "Email Id").grid(row = 3, sticky = W)

e1 = Entry()
e1.grid(row = 0 , column = 1)
e1.insert(0 , "ROIHIT ")

e2 = Entry()
e2.grid(row = 1 , column = 1)
e2.insert(0, "SONI")

e3 = Entry()
e3.grid(row = 2 , column = 1)
e3.insert(0, "7891938911")

e4 = Entry()
e4.grid(row = 3 , column = 1)
e4.insert(0, "rsony.721@gmail.com")

def reset(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)




b= Button(root, text = "RESET")
b.grid(row = 4 , column = 0)
b.bind("<Button-1>",reset)












root.mainloop()