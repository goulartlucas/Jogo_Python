import random

class Aventureiro:
    def __init__(self, nome):
        self.nome = nome
        self.posicao = [0,0]
        self.vida = random.randint(100, 120)
        self.vida_atual = self.vida
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.mochila = []

    def adcionar_item_mochila(self, item):
        self.mochila.append((item))
    
    def usar_item(self, item):
        if item.tipo == 'vida':
            vida = self.vida_atual
            self.vida_atual = min(self.vida_atual + (20 * item.intensidade), self.vida)
            return f"{self.vida_atual} + {20 * item.intensidade} > {self.vida_atual}/{self.vida}"
        elif item.tipo == 'força':
            forca = self.forca
            self.forca += item.intensidade
            return f"{forca} + {item.intensidade} > {self.forca}"
        elif item.tipo == 'defesa':
            defesa = self.defesa
            self.defesa += item.intensidade
            return f"{defesa} + {item.intensidade} > {self.defesa}"
        

    def verifica_vida(self):
        if self.vida_atual <= 0:
            return 0
        else :return self.vida_atual

    def ver_atributos(self):
        print("")
        print(f"Sua vida: {self.verifica_vida()}/{self.vida}")
        print(f"Sua Forca: {self.forca}")
        print(f"Sua Defesa: {self.defesa}")
