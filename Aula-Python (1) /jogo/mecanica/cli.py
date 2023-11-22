import random

from jogo.ativos import item, mapa, tesouro
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro

def interagir_item(p1):
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """
    print("")
    print ("~ Você abriu a Mochila")
    print("")
    itens = []
    for i, j in enumerate(p1.mochila):
        itens.append(i+1)
        print(f"{i+1} ~ {j.nome}")
        print("")
    while True:
        
        op = int(input("Insira o indice do item ou 0 pra Sair: "))
        if op in itens:
            item = p1.mochila[op - 1]
            efeito = p1.usar_item(item)
            print("")
            print(f"Você usou um(a) {item.nome}")
            print(efeito)
            print("")
        elif op == 0:
            print("")
            print("~ Você Cancelou")
            print("")
            break
        else:
            print("")
            print("~ Você não possue esse Item...")
            print("")
            




def movimentar(p1, dir):
    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """
    
    if dir == 'W':
        p1.posicao[1] = max(p1.posicao[1] - 1, 0)
    elif dir == 'A':
        p1.posicao[0] = max(p1.posicao[0] - 1, 0)
    elif dir == 'S':
        p1.posicao[1] =  min(p1.posicao[1] + 1, 9)
    elif dir == 'D':
        p1.posicao[0] = min(p1.posicao[0] + 1, 9)

    efeito = random.choices([1,2,3],[0.2, 0.4, 0.4], k=1)[0]
    if efeito == 1:
        item1 = item.Item( "força", 1)
        item2 = item.Item( "força", 2)
        item3 = item.Item( "vida", 1)
        item4 = item.Item( "vida", 2)
        item5 = item.Item( "defesa", 1)

        itens = [item1,item2,item3,item4,item5]
        
        i = random.choices(itens,[0.10, 0.05, 0.50, 0.30, 0.05], k=1)[0]
        p1.adcionar_item_mochila(i)
        print("")
        print(f"+ {i.nome}")
        pass
    if efeito == 2:
        combate.combate(p1, monstro.Monstro("Monstro"))
    if efeito == 3:
        pass
    return True

def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = aventureiro.Aventureiro(nome)
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.desenhar(p1, tes)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            
            if movimentar(p1, op):
                mapa.desenhar(p1, tes)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break
