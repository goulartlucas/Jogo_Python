import random

class Monstro:
    def __init__(self, nome):
        self.nome = nome
        self.vida = random.randint(10, 100)
        self.vida_atual = self.vida
        self.forca = random.randint(5, 25)
        self.defesa = random.randint(5, 10)
    def verifica_vida(self):
        if self.vida_atual <= 0:
            return 0
        else :return self.vida_atual

    def ver_atributos(self):
        print("")
        print(f"Vida do monstro: {self.verifica_vida()}/{self.vida}")
        print(f"Forca do monstro: {self.forca}")
        print(f"Defesa do monstro: {self.defesa}")