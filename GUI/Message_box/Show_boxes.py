from tkinter import *
import tkinter.messagebox


root = Tk()
root.title("Demo of boxes")
root.geometry("300x130+100+100")

def show():
    tkinter.messagebox.showinfo(title = "title bar", message="Information!!")

    tkinter.messagebox.showwarning(title="Title bar", message = "Warning!!")

    tkinter.messagebox.showerror(title="Title bar", message = "Error!!")




b = Button(text="Message_box", command = show)
b.pack()


root.mainloop()
