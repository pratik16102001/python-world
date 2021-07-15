from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("title","this is awesome")
respond = tkinter.messagebox.askquestion("Question 1","do you like cofee")

if respond == 'yes':
    print("here is a coffee for you")

root.mainloop()