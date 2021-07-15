from tkinter import *
def function1():
    print("Menu is working")


root = Tk()
mymenu = Menu(root)
root.config(menu=mymenu)

submenu = Menu(mymenu)
mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="new project", command=function1())

newmenu = Menu(mymenu)
mymenu.add_cascade(label="view", menu=newmenu)
newmenu.add_command(label="tool window", command=function1())

toolbar = Frame(root, bg="pink")
insertbutton = Button(toolbar, text="insert Files", commmand=function1())
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1())
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)
root.mainloop()