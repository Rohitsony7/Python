from tkinter import *
import tkinter.messagebox

root = Tk()
root.title("Demo")
root.geometry("300x300+100+100")

def show():
     a= tkinter.messagebox.askyesnocancel(title = "Title bsr", message="Do you want to exit ?")

     print(a)

     if a ==True:
         root.destroy()

     elif a  == False:
         root1 = Tk()

         root.title("No")
         e1 =Text(root1)
         e1.insert(END, "Why do you want to west your time, come out from the box, go for a walk, read a novel, Do meditate, and chears to life.")
         e1.pack()

b = Button(text = "Click to msg", command = show, bg="PINK").pack()
e1= Text(bg= "Pink")
e1.pack()

root.mainloop()