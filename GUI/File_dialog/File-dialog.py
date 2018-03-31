from tkinter import *
import tkinter.filedialog

root = Tk()
root.geometry("300x300+100+100")




def show():
     file = tkinter.filedialog.askopenfile()
     print(file)

     filename= file.name

     print(filename)

     l = Label(text =  filename).pack()

     f = open(filename)
     t= Text(root ) #  can be changed accordingly(height = 50 and width = 50)
     t.insert(END, f.read())
     t.pack()




b= Button(text = "File_dialog", command = show).pack()

root.mainloop()

