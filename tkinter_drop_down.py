from tkinter import *

def function1():
    print("Menu is working")

root = Tk()
#main menu creation
mymenu = Menu(root)
root.config(menu=mymenu)

#passing the submenu at the main menu
submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="new project", command=function1())
submenu.add_command(label="save", command=function1())
submenu.add_command(label="save as", command=function1())
submenu.add_command(label="rename project", command=function1())
submenu.add_command(label="open recent", command=function1())
submenu.add_separator()
submenu.add_command(label="Exit", command=function1())



#second menu
newmenu = Menu(mymenu)
mymenu.add_cascade(label="view", menu=newmenu)
newmenu.add_command(label="tool window", command=function1())
newmenu.add_command(label="Appereance", command=function1())
newmenu.add_separator()
newmenu.add_command(label="quick swicth theme", command=function1())
newmenu.add_command(label="opem editor", command=function1())

#third menu
newmenu1 = Menu(mymenu)
mymenu.add_cascade(label="Navigate", menu=newmenu1)
newmenu1.add_command(label="class", command=function1())
newmenu1.add_command(label="file", command=function1())
newmenu1.add_command(label="symbol", command=function1())
newmenu1.add_separator()
newmenu1.add_command(label="exit", command=function1())

#fourth menu
newmwnu2 = Menu(mymenu)
mymenu.add_cascade(label="code", menu=newmwnu2)
newmwnu2.add_command(label="instpect code ", command=function1())
newmwnu2.add_command(label="code clean up", command=function1())
newmwnu2.add_command(label="code silent clean up", command=function1())
newmwnu2.add_command(label="inspector", command=function1())
newmwnu2.add_separator()
newmwnu2.add_command(label="Run", command=function1())
newmwnu2.add_command(label="exit", command=function1())

root.mainloop()
