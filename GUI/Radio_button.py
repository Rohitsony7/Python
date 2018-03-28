from tkinter import *

root = Tk()


root.title("RADIO_BUTTON")



def show(event):
    value = v.get()

    if (value ==1):
        obj = Tk()
        obj.title("python")
        Label(obj, text = "PYTHON").pack()

    if value == 2:
        Label(text = "JAVA clicked").pack()

    if value == 3:
        Label( text = "ML clicked").pack()

    if value == 4:
        Label( text = "AI clicked").pack()

   #   print("ANY RADIO BUTTON CLICKED")

v = IntVar()
Label(root,text="Choose your Course for internship", justify = LEFT).pack()


r1 = Radiobutton(root , value = 1,  variable = v , fg = "blue", justify = LEFT, text= "PYTHON")
r1.bind("<Button-1>" , show)
r2 = Radiobutton(root ,text= "JAVA", value = 2, variable = v, fg = "red", justify = LEFT)
r2.bind("<Button-1>" , show)
r3 = Radiobutton(root ,text= "ML", value = 3, variable = v, fg = "green", justify = LEFT)
r3.bind("<Button-1>" , show)
r4 = Radiobutton(root , text= "AI", value = 4, variable = v, fg = "cyan", justify = LEFT )
r4.bind("<Button-1>" , show)

r1.pack(anchor = W)  #  , padx =30, pady = 40 for (x,y) parameter
r2.pack(anchor = W)
r3.pack(anchor = W)
r4.pack(anchor = W)


root.mainloop()
