from tkinter import *
x=" "
def zero():
    x=x+"0"
    myLabel.configure(text="x")
def one():
    x=x+"1"
    myLabel.configure(text="x")
def two():
    x=x+"2"
    myLabel.configure(text="x")
def three():
    x=x+"3"
    myLabel.configure(text="x")
def four():
    x=x+"4"
    myLabel.configure(text="x")
def five():
    x=x+"5"
    myLabel.configure(text="x")
def six():
    x=x+"6"
    myLabel.configure(text="x")
def seven():
    x=x+"7"
    myLabel.configure(text="x")
def eight():
    x=x+"8"
    myLabel.configure(text="x")
def nine():
    x=x="9"
    myLabel.configure(text="x")




mainWindow = Tk()
mainWindow.configure(bg="black")
myLabel = Label(mainWindow, text=" ")
myLabel.grid(column=0, row=0, padx=10, pady=10)

zero = Button(mainWindow, text="0", command=zero)
zero.grid(column=1, row=4, padx=10, pady=10)

one = Button(mainWindow, text="1", command=one)
one.grid(column=0, row=3, padx=10, pady=10)

two = Button(mainWindow, text="2", command=two)
two.grid(column=1, row=3, padx=10, pady=10)

three = Button(mainWindow, text="3", command=three)
three.grid(column=2, row=3, padx=10, pady=10)

four = Button(mainWindow, text="4", command=four)
four.grid(column=0, row=2, padx=10, pady=10)

five = Button(mainWindow, text="5", command=five)
five.grid(column=1, row=2, padx=10, pady=10)

six = Button(mainWindow, text="6",  command=six)
six.grid(column=2, row=2, padx=10, pady=10)

seven = Button(mainWindow, text="7",  command=seven)
seven.grid(column=0, row=1, padx=10, pady=10)

eight = Button(mainWindow, text="8",  command=eight)
eight.grid(column=1, row=1, padx=10, pady=10)

nine = Button(mainWindow, text="9",  command=nine)
nine.grid(column=2, row=1, padx=10, pady=10)

mainWindow.mainloop()