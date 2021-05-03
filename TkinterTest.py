from tkinter import *

top = Tk()
L1 = Label(top, text="Hello, world!")
E1 = Entry(top, bd = 5)


L1.grid(column=0, row=1)
E1.grid(column=0,row=2)

    
#Must Be last
top.mainloop()
