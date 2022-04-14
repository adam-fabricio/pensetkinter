#!/bin/python3
#utf-8

from tkinter import *

class MyApp:
    """Classe que irá gerar as janelas do Tkinter."""
    
    def __init__(self, parent):
        """Função que inícia a classe."""
        #  Define parent como uma variável da classe.
        self.my_parent = parent
        #  Cria o recepiente e recebe como parâmetro a raiz.
        self.meu_recepiente = Frame(parent)
        #  Empacota o recepiente.
        self.meu_recepiente.pack()
        
        #  Cria um botao chamado "botao1"
        self.botao1 = Button(self.meu_recepiente)
        #  Escreve um texto no botão e define a cor de fundo do botão.
        self.botao1.configure(text="OK", background="green")
        #  Empacota o botão e coloca ele no lado esquerdo.
        self.botao1.pack(side=LEFT)
        #  Força o foco do botão nele.
        self.botao1.focus_force()
        #  Define uma função para o botão ao apertar enter.
        self.botao1.bind("<Return>", self.botao1_click)
        #  Define uma função ao apertar o botão do mouse.
        self.botao1.bind("<Button-1>", self.botao1_click)
        
        
        #  Cria um botão chamado botao2.
        self.botao2 = Button(self.meu_recepiente)
        #  Escreve um texto no botão e define cor de fundo no botão.
        self.botao2.configure(text="Cancelar", background="red")
        #  Empacota o botão colocando ele do lado esquerdo.
        self.botao2.pack(side=RIGHT)
        #  Define uma função ao apertar o enter no botão.
        self.botao2.bind("<Return>", self.botao2_click)
        #  Define uma função ao apertar o botão do mouse.
        self.botao2.bind("<Button-1>", self.botao2_click)
        
        
    
    def botao1_click(self, event):
        """Função de quando apertar o botão 1."""
        
        #  Envia o evento para gerar relatorio.
        relatorio_do_evento(event)
        #  Caso o fundo do botao1 for verde.
        if self.botao1["background"] == "green":
            #  Troca a cor para amarelo.
            self.botao1["background"] = "yellow"
        else:
            #  Se não muda  a cor de fundo para verde.
            self.botao1["background"] = "green"
    
    
    def botao2_click(self, event):
        """Função de quando apertar o botao 2."""
        
        #  Envia o evento para uma função que irá imprimir o reloatorio.
        relatorio_do_evento(event)
        #  Fecha a janela.
        self.my_parent.destroy()


def relatorio_do_evento(evento):
    """Função que irá exibir os atributos do evento."""
    
    nome_do_evento = {"2": "KeyPress", "4": "ButtonPress"}
    print(f"Time: {str(evento.time)}")
    print(f"EventType: {str(evento.type)}")
    print(f"EventName: {str(evento.type)}")
    print(f"EventWidgetId: {str(evento.widget)}")
    print(f"EventKeySymbol: {str(evento.keysym)}")

root = Tk()
myapp = MyApp(root)
root.mainloop()
