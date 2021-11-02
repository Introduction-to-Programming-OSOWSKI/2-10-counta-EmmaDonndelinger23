from tkinter import *
main = Tk()
main.title("Secret passwod")
main.resizable(False, False)
def show():
    myEntry.configure(show="")
def hide():
    myEntry.configure(show="*")

myEntry = Entry(main, font=("courier", 30), bg="#2e2e2e", fg="limegreen", selectbackground="yellow", selectforeground="pink", show="*")
myEntry.grid(column=1, row=0)

passLabel = Label(main, text="password", bg="#2e2e2e", fg="darkgrey", font=("courier,20"))
passLabel.grid(column=0, row=0)

showPassword = Button(main, text="Show", command=show)
showPassword.grid(column=0, row=2)

hidePassword = Button(main, text="Hide", command=hide)
hidePassword.grid(column=0, row=3)

main.mainloop()
