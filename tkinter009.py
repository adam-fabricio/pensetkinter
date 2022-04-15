#!/bin/python3


from tkinter import *

class MyApp:
    def __init__(self, parent):
        self.my_parent = parent
        
        self.meu_recipiente = Frame(parent)
        self.meu_recipiente.pack()
        
        nome_botao = "OK"
        self.button1 = Button(self.meu_recipiente, 
                        command=self.buttonHandler(nome_botao, 1, "Boas coisas."))
        self.button1.configure(text=nome_botao, background="green")
        self.button1.pack(side=LEFT)
        self.button1.focus_force()
        #self.button1.bind("<Return>", 
        #                  self.buttonHandler_a(nome_botao, 1, "Boas coisas."))
        
        nome_botao = "Cancel"
        self.button2 = Button(self.meu_recipiente, 
                        command=self.buttonHandler(nome_botao, 2, "Coisas Ruins."))
        self.button2.configure(text=nome_botao, background="red")
        self.button2.pack(side=LEFT)
        #self.button2.bind("<Return>", 
        #                  self.buttonHandler_a(nome_botao, 1, "Boas coisas."))
        

    def buttonHandler(self, arg1, arg2, arg3):
        print(f"Manipulador do botão recebeu {arg1}, {arg2} e {arg3}")
    
    def buttonHandler_a(self, event, arg1, arg2, arg3):
        print(f"Manipulador_a do botão recebeu {arg1}, {arg2} e {arg3}")
        self.buttonHandler(arg1, arg2, arg3)

print("\n"*100)
print("Starting program tt0077.")
root = Tk()
myapp = MyApp(root)
print("Pronto para começar a executar o loop do evento.")
root.mainloop()
print("Terminado a execução do loope de evento.")

        
    
    
        
        