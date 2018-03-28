from tkinter import *

root = Tk()

root.title("Demo if CheckButton")

root.geometry("400x300+100+100")

Label(root, text = "Choose your skills").pack(anchor = W)

def show(event):
    print(v1.get(), v2.get(), v3.get(), v4.get())



v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

Checkbutton(root, text = "PYTHON", variable = v1, fg = "orange").pack(anchor = W)
Checkbutton(root, text = "JAVA", variable = v2, fg = "RED").pack(anchor = W)
Checkbutton(root, text = "MYSQL", variable = v3, fg = "BLUE").pack(anchor = W)
Checkbutton(root, text = "DSA", variable = v4, fg = "GREEN").pack(anchor = W)

b1 = Button(root, text = "CLICK", bg= "PINK")
b1.pack(anchor = W)
b1.bind("<Button-1>",show)

root.mainloop()


