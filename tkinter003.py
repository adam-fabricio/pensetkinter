#!/bin/python3

from tkinter import *

class MyApp:
    def __init__(self, my_parent):
        self.meu_recepiente1 = Frame(my_parent)
        self.meu_recepiente1.pack()
        
        self.button1 = Button(self.meu_recepiente1)
        self.button1["text"] = "Hello, World"
        self.button1["background"] = "green"
        self.button1.pack(side=LEFT)
        
        self.button2 = Button(self.meu_recepiente1)
        self.button2.configure(text="Saia do circo!")
        self.button2.configure(background="tan")
        self.button2.pack(side=LEFT)
        
        self.button3 = Button(self.meu_recepiente1)
        self.button3.configure(text="Junte-se a mim!", background="cyan")
        self.button3.pack(side=LEFT)
        
        self.button4 = Button(self.meu_recepiente1, text="Tchau!!!!", 
                              background="red")
        self.button4.pack(side=LEFT)

root = Tk()
myapp = MyApp(root)
root.mainloop()
