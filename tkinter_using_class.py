from tkinter import *

class Mybutton:
    def __init__(self,rootone):
        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="Click here", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="Exit", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("Button Clicked")

root = Tk()

b = Mybutton(root)

root.mainloop()
