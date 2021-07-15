from tkinter import *
root = Tk()

newframe = Frame(root)
newframe.pack()

otherframe = Frame(root)
otherframe.pack(side=BOTTOM)

button1 = Button(newframe, text="click here", fg="Red")
button2 = Button(newframe, text="click here", fg="blue")

button1.pack()
button2.pack()

root.mainloop()