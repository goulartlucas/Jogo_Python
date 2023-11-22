import random
class Tesouro:
    def __init__(self):
        self.posicao = self.gera_posicao()

    def gera_posicao(self):
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if x == 1 and y == 1:
            self.gera_posicao()
        else :return [x,y]
