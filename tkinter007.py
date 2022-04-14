#!/bin/python3

from tkinter import *

class MyApp:
    """Classe do meu app."""
    
    def __init__(self, parent):
        """Função de inicialização da classe."""
        self.my_parent = parent
        self.meu_recipiente = Frame(parent)
        self.meu_recipiente.pack()
        
        self.button1 = Button(self.meu_recipiente, command=self.botao1_clique)
        self.button1.bind("<Return>", self.botao1_clique_a)
        self.button1.configure(text="OK", background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()
        
        self.button2 = Button(self.meu_recipiente, command=self.botao2_clique)
        self.button2.bind("<Return>", self.botao2_clique_a)
        self.button2.configure(text="CANCEL", background="red")
        self.button2.pack(side=RIGHT)
        
    def botao1_clique(self):
        """Evento quando o botão for acionado."""
        print("Manipulador do evento do botão1.")
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
    
    def botao2_clique(self):
        """Evento quando o botao 2 for acionado."""
        print("Manupulador do evento do botão 2.")
        self.my_parent.destroy()
    
    def botao1_clique_a(self, event):
        """Evento empacotado1."""
        print("manupulador de evento botao1_clique_a embrulhado.")
        self.botao1_clique()
    
    def botao2_clique_a(self, event):
        """Evento que reenvia a requisição para outra função."""
        print("Manipulador de evento botao2_clique_a embrulhado.")
        self.botao2_clique()


root = Tk()
myapp = MyApp(root)
root.mainloop()