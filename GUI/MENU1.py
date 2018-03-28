from tkinter import *

root = Tk()
root.title("DEMO")
root.geometry("300x200+100+100")

mymenu = Menu()

mymenu.add_cascade(label = "FILE")
mymenu.add_cascade(label = "EDIT")
mymenu.add_cascade(label = "HELP")
mymenu.add_cascade(label = "VIEW")

root.config(menu = mymenu) # TO ADD THR MENU ONTHE WINDOW
root.mainloop()