from tkinter import *
root = Tk()

label1 = Label(root, text="First", bg="red", fg="White")
label1.pack(fill=X)

label2 = Label(root, text="second", bg="blue", fg="Green")
label2.pack(side=LEFT,fill=Y)

root.mainloop()