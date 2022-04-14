#!/bin/python3


from tkinter import *

class MyApp:
    def __init__(self, parent):
        
        self.meu_ultimo_botao_pressionado = None
        
        self.my_parent = parent  
        self.meu_recipiente = Frame(parent)
        self.meu_recipiente.pack()
        
        self.botao_amarelo = Button(self.meu_recipiente, 
                                    command=self.botao_amarelo)
        self.botao_amarelo.configure(text="AMARELO", background="yellow")
        self.botao_amarelo.pack(side=LEFT)
        
        self.botao_vermelho = Button(self.meu_recipiente, 
                                    command=self.botao_vermelho)
        self.botao_vermelho.configure(text="VERMELHO", background="red")
        self.botao_vermelho.pack(side=LEFT)
        
        self.botao_branco = Button(self.meu_recipiente, 
                                    command=self.botao_branco)
        self.botao_branco.configure(text="BRANCO", background="white")
        self.botao_branco.pack(side=LEFT)
        
        
    def botao_amarelo(self):
        print("Botão amarelo foi clicado. O botão anterior clicado foi")
        print(self.meu_ultimo_botao_pressionado)
        self.meu_ultimo_botao_pressionado = "Amarelo"
    
    
    def botao_vermelho(self):
        print("Botão vermelho foi clicado. O botão anterior clicado foi")
        print(self.meu_ultimo_botao_pressionado)
        self.meu_ultimo_botao_pressionado = "Vermelho"
        
        
    def botao_branco(self):
        print("Botão branco foi clicado. O botão anterior clicado foi")
        print(self.meu_ultimo_botao_pressionado)
        self.meu_ultimo_botao_pressionado = "Branco"


print("\n"*100)
print("Começando......")
root = Tk()
myapp = MyApp(root)
root.mainloop()
print("...Done")
    