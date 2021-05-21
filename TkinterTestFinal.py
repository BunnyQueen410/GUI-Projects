from tkinter import *
import random

List=[]
top = Tk()
playerRolls = []
rollTotal = 0
dieType = 0

def mainMenu():
    clearWindow()
    LMain = Label(top, text="Block 5 GUI")
    LMain.grid(column=0, row=1)

    B1Main= Button(text = "Week one", bg="#cff1fa", command = week1)
    B1Main.grid(column=0, row=3)

    B2Main= Button(text = "Week two", bg="#dae6f7", command = week2)
    B2Main.grid(column=0, row=4)

    B3Main= Button(text = "Week three", bg="#eedcf7", command = week3)
    B3Main.grid(column=0, row=5)
def results():
    print(List)


def expotList():
    with open('test.txt', 'w') as f:
        for item in List:
            f.write("%s / " % item)
def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()
def week1():
    clearWindow()
    def addToList():
        List.append(E1.get())
        E1.delete(0, END)


    #this is a Label Widget
    L1 = Label(top, text="Grocery List")
    L1.grid(column=0, row=1)

    #this is a entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column=0,row=2)

    #This is a button
    B1 = Button(text ="    See your List    ", bg="#d0b8f2", command=results)
    B1.grid(column=0, row=3)

    B2 = Button(text=" + ",bg="#b8f2ea",command=addToList)
    B2.grid(column=1,row=2)

    B3 = Button(text=" Export your list ", bg="#d3f0d5", command=expotList)
    B3.grid(column =1, row =3)

    Bclear = Button(text = "Main Menu", bg = "white", command=mainMenu)
    Bclear.grid(column = 3, row =1)

def week2():
    def rollDice():
        dieType = E1W2.get()
        rollTimes = E2W2.get()
        clearWindow()

        try:
            for x in range (0, int(rollTimes)):
                playerRolls.append(random.randint(1, int(dieType)))

            L4W2 = Label(top, text = "Here are your rolls!")
            L4W2.grid(column = 0, row=1)

            L5W2 = Label(top, text = "{}".format(playerRolls))
            L5W2.grid(column = 0, row = 2)

            B2W2 = Button(text = "Return to Main menu", bg = "#b3f2e7", command = mainMenu)
            B2W2.grid(column = 0, row = 3)
        except:
            L6 = Label(top, text = "That didnt seem to work, try again")
            L6.grid(column = 1, row = 1)
            B3 = Button(text = "Click here to try again", bg = "#ebffd1", command = week2)
            B3.grid(column = 1, row = 3)
            B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
            B4.grid(column = 1, row = 4)


    clearWindow()
    L1W2 =  Label(top, text="Dice roller program")
    L1W2.grid(column = 0, row =1)

    L2W2=Label(top, text="How many sides")
    L2W2.grid(column=0, row=2)

    L3W2 = Label(top, text = "How many rolls?")
    L3W2.grid(column = 2, row = 2)

    E1W2 = Entry(top, bd =5)
    E1W2.grid(column = 0 ,row = 3)

    E2W2 = Entry(top, bd=5)
    E2W2.grid(column=2, row=3)

    B1W2 = Button(text= "     Roll!     ", bg= "#b3f2e7", command = rollDice)
    B1W2.grid(column=2, row=4)





























def week3():
        
    def You():
        def Guess():
            def Guess2():
                def Guess3():
                    def Guess4():
                        def GuessLast():
                            Guess = E3W9.get()
                            clearWindow()        
                            if int(Guess) == magic:
                                clearWindow()
                                LWin =Label(top, text="You guessed the number!!!")
                                LWin.grid(column=1, row = 1)
                                B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                                B4.grid(column = 1, row = 4)
                            else:
                                clearWindow()
                                L1W90=Label(top, text="Im sorry you lost. Your number was {}".format(magic))
                                L1W90.grid(column=1, row=1)
                                B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                                B4.grid(column = 1, row = 4)
                        Guess = E3W6.get()
                        clearWindow()        
                        if int(Guess) == magic:
                            clearWindow()
                            LWin =Label(top, text="You guessed the number!!!")
                            LWin.grid(column=1, row = 1)
                            B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                            B4.grid(column = 1, row = 4)
                        elif int(Guess)< magic:
                            Llower=Label(top, text="""Try again your number is Higher

                            """)
                            Llower.grid(column=1, row =1)
                            L4W2 = Label(top, text = "What is your last guess")
                            L4W2.grid(column = 2, row = 2)
                            E3W9 = Entry(top, bd=5)
                            E3W9.grid(column=2, row=3)
                            B3W3=Button(text="Guess", command = GuessLast)
                            B3W3.grid(column =2, row=4)
                        else:
                            Lhigher=Label(top, text="""Try Lower this time

                            """)
                            Lhigher.grid(column=1,row=1)
                            L3W2 = Label(top, text = "What is your last guess")
                            L3W2.grid(column = 2, row = 2)
                            E3W9 = Entry(top, bd=5)
                            E3W9.grid(column=2, row=3)
                            B2W3=Button(text="Guess",command = GuessLast)
                            B2W3.grid(column =2, row=4)









                        
                    Guess = E3W5.get()
                    clearWindow()        
                    if int(Guess) == magic:
                        clearWindow()
                        LWin =Label(top, text="You guessed the number!!!")
                        LWin.grid(column=1, row = 1)
                        B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                        B4.grid(column = 1, row = 4)
                    elif int(Guess)< magic:
                        Llower=Label(top, text="""Try again your number is Higher

                        """)
                        Llower.grid(column=1, row =1)
                        L4W2 = Label(top, text = "What is your next guess")
                        L4W2.grid(column = 2, row = 2)
                        E3W6 = Entry(top, bd=5)
                        E3W6.grid(column=2, row=3)
                        B3W3=Button(text="Guess", command = Guess4)
                        B3W3.grid(column =2, row=4)
                    else:
                        Lhigher=Label(top, text="""Try Lower this time

                        """)
                        Lhigher.grid(column=1,row=1)
                        L3W2 = Label(top, text = "What is your next guess")
                        L3W2.grid(column = 2, row = 2)
                        E3W6 = Entry(top, bd=5)
                        E3W6.grid(column=2, row=3)
                        B2W3=Button(text="Guess",command = Guess4)
                        B2W3.grid(column =2, row=4)



                        
                Guess = E2W4.get()
                clearWindow()        
                if int(Guess) == magic:
                    clearWindow()
                    LWin =Label(top, text="You guessed the number!!!")
                    LWin.grid(column=1, row = 1)
                    B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                    B4.grid(column = 1, row = 4)
                elif int(Guess)< magic:
                    Llower=Label(top, text="""Try again your number is Higher

                    """)
                    Llower.grid(column=1, row =1)
                    L4W2 = Label(top, text = "What is your next guess")
                    L4W2.grid(column = 2, row = 2)
                    E3W5 = Entry(top, bd=5)
                    E3W5.grid(column=2, row=3)
                    B3W3=Button(text="Guess", command = Guess3)
                    B3W3.grid(column =2, row=4)
                else:
                    Lhigher=Label(top, text="""Try Lower this time

                    """)
                    Lhigher.grid(column=1,row=1)
                    L3W2 = Label(top, text = "What is your next guess")
                    L3W2.grid(column = 2, row = 2)
                    E3W5 = Entry(top, bd=5)
                    E3W5.grid(column=2, row=3)
                    B2W3=Button(text="Guess", command = Guess3)
                    B2W3.grid(column =2, row=4)


            Guess = E2W2.get()
            clearWindow()        
            if int(Guess) == magic:
                clearWindow()
                LWin =Label(top, text="You guessed the number!!!")
                LWin.grid(column=1, row = 1)
                B4 = Button(text = "Click here to return to main menu", bg = "#ffebc7", command = mainMenu)
                B4.grid(column = 1, row = 4)
            elif int(Guess)< magic:
                Llower=Label(top, text="""Try again your number is Higher

                """)
                Llower.grid(column=1, row =1)
                L4W2 = Label(top, text = "What is your next guess")
                L4W2.grid(column = 2, row = 2)
                E2W4 = Entry(top, bd=5)
                E2W4.grid(column=2, row=3)
                B3W3=Button(text="Guess", command = Guess2)
                B3W3.grid(column =2, row=4)
            else:
                Lhigher=Label(top, text="""Try lower this time

                """)
                Lhigher.grid(column=1,row=1)
                L3W2 = Label(top, text = "What is your next guess")
                L3W2.grid(column = 2, row = 2)
                E2W4 = Entry(top, bd=5)
                E2W4.grid(column=2, row=3)
                B2W3=Button(text="Guess",command = Guess2)
                B2W3.grid(column =2, row=4)





        














                

        clearWindow()
        magic =(random.randint(1,100))
        L2W3=Label(top,text = """Hello, I bet you cant guess the number Im thinking ^-^
The two rules:
You get five chances then its game over,
It will of be a number between 1 and 100""")
        L2W3.grid(column=1,row=0)
        L3W2 = Label(top, text = "What is your guess")
        L3W2.grid(column = 2, row = 2)
        E2W2 = Entry(top, bd=5)
        E2W2.grid(column=2, row=3)
        B2W3=Button(text="Guess", command = Guess)
        B2W3.grid(column =2, row=4)

    You()

if __name__ == "__main__":
    mainMenu()


#Must Be last
top.mainloop()
