from tkinter import *

root = Tk()
root1 = Tk()

root.title("Demo of Event")
root.geometry("400x400+300+100")

l1 = Label(root,text="Enter Name")
l1.place(x =20, y = 10)

a = StringVar()


def show(event):
    b = a.get()
    l2 = Label(root1, text=b)
    l2.pack()

    print("Button clicked",)



e1 = Entry(root, textvariable = a)
e1.place(x= 100, y = 10)

b1 = Button(root, text="SAVE")
b1.bind("<Button - 1>", show)
b1.bind("<Button - 2>", show)
b1.bind("<Button - 3>", show)

b1.place(x= 250, y =10)

root.mainloop()
