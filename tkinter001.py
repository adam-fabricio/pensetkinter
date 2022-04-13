#!/bin/python3

from tkinter import *

class MyApp:
    def __init__(self, my_parent):
        self.meu_recepiente1 = Frame(my_parent)
        self.meu_recepiente1.pack()
        
        self.button1 = Button(self.meu_recepiente1)
        self.button1["text"] = "Hello, World"
        self.button1["background"] = "green"
        self.button1.pack()

root = Tk()
myapp = MyApp(root)
root.mainloop()
