#!/bin/python3


from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.my_parent = parent
        self.meu_recipiente = Frame(parent)
        self.meu_recipiente.pack()
        
        #  ------------------------Botão 1 -------------------
        
        nome_botao = "OK"
        
        #  Comand binding
        self.botao1 = Button(self.meu_recipiente,
                             command=lambda
                             arg1=nome_botao, arg2=1, arg3="Boas Coisas" :
                             self.manipulador_botao(arg1, arg2, arg3)
                             )
        #  Event biding - transmitindo o evento como um argumento
        self.botao1.bind("<Return>", 
                         lambda 
                         arg1=nome_botao, arg2=1, arg3="Boas Coisas" : 
                         self.manipulador_botao_a(event, arg1, arg2, arg3)
                         )
        
        self.botao1.configure(text=nome_botao, background="green")
        self.botao1.pack(side=LEFT)
        self.botao1.focus_force()
        
        #  ---------------------------------Botao 2 ----------------
        nome_botao = "Cancel"
        
        #  Comando binding
        self.botao2 = Button(self.meu_recipiente, 
                             command=lambda
                             arg1=nome_botao, arg2=2, arg3="Coisas Ruins" :
                             self.manipulador_botao(arg1, arg2, arg3)
                             )
        #  Event binding - sem passar o evento como um argumento
        self.botao2.bind("<Return>",lambda
                         event, arg1=nome_botao, arg2=2, arg3="Coisas Ruins" :
                         self.manipulador_botao(arg1, arg2, arg3)
                         )
        self.botao2.configure(text=nome_botao, background="red")
        self.botao2.pack(side=LEFT)
        
    def manipulador_botao(self, argumento1, argumento2, argumento3):
        print("Manipulador do botão reecbe argumentos:",
              argumento1, argumento2, argumento3)
    
    def manipulador_botao_a(self, event, argumento1, argumento2, argumento3):
        print("Manipulador_a recebeu como argumento", event, 
              self.manipulador_botao(argumento1, argumento2, argumento3))


print("\n"*100)
print("Iniciando o programa................")

root = Tk()
myapp = MyApp(root)

print("Pronto para começar o programa.")
root.mainloop()
print("Terminado de executar o programa.")
