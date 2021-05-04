from tkinter import *

List=[]
top = Tk()
def results():
    result = E1.get()
    print(List)
def addToList():
    List.append(E1.get())
#this is a Label Widget
L1 = Label(top, text="Grocery List")
L1.grid(column=0, row=1)

#this is a entry widget
E1 = Entry(top, bd = 5)
E1.grid(column=0,row=2)

#This is a button
B1 = Button(text ="    See your List    ", bg="green", command=results)
B1.grid(column=0, row=3)

B2 = Button(text="Add to List",bg="blue",command=addToList)
B2.grid(column=1,row=2)

    
#Must Be last
top.mainloop()
