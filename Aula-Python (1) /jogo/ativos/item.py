import random


class Item():
    def __init__(self,tipo,intensidade):
        self.tipo = tipo
        self.intensidade = intensidade
        self.nome = self.get_nome()
 
        

    def get_nome(self):
        return "Poção de " + self.tipo + " intensidade " + str(self.intensidade)

