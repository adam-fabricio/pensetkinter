#!/bin/python3

from tkinter import *

class MyApp:
    """Classe do aplicativo padrão."""
    def __init__(self, parent):
        """Inicio da classe."""
        #  salva em uma variavél da classe quem é o processo pai.
        self.my_parent = parent
        #  Cria um recepiente no processo pai.
        self.meu_recepiente1 = Frame(parent)
        self.meu_recepiente1.pack()
        
        #  Cria um botão no recepiente.
        self.button1 = Button(self.meu_recepiente1)
        #  Define o nome do botão e a cor de fundo.
        self.button1.configure(text="OK", background="green")
        #  Define onde o botão será exibido.
        self.button1.pack(side=LEFT)
        #  Ao clicar com o botão direito do mouse executar função.
        self.button1.bind("<Button-1>", self.button1_click)
        
        #  Cria outro botão no recepiente.
        self.button2 = Button(self.meu_recepiente1)
        #  Configura o botão com o nome e cor de fundo.
        self.button2.configure(text="Cancel", background="red")
        #  Define que o botão ficará a direita.
        self.button2.pack(side=RIGHT)
        #  Ao clicar com o botão direito do mouse executar função.
        self.button2.bind("<Button-1>", self.button2_click)
        
    def button1_click(self, evento):
        """Define o que fazer ao clicar o botão1."""
        if self.button1["background"] == "green":
            self.button1["background"] = "yellow"
        else:
            self.button1["background"] = "green"
        
    def button2_click(self, evento):
        """Fecha o programa."""
        self.my_parent.destroy()

#  Define que o root é uma instância Tk().
root = Tk()
#  Instancia myapp como um objeto iniciando com o parâmetro "root".
myapp = MyApp(root)
#  Cria o loop do programa.
root.mainloop()
