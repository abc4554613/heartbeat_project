from tkinter import *


def printEntry():
    print(name.get())


window = Tk()
name = StringVar()
btn = Button(window, command=printEntry)
nameEntry = Entry(window, textvariable=name)
nameEntry.config(font=("Arial", 30))
window.mainloop()
