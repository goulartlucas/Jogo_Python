import random
import time
from jogo.ativos import mapa
from jogo.mecanica import cli

def combate(p1, monstro):

    mapa.cria_divisao_texto("}= Combate ={","<=","==","=>")
    mapa.cria_divisao_texto("ᕕ( @_@)ᕗ  X  (◣_◢ )ψ")
    
    p1.ver_atributos()
    monstro.ver_atributos()
    
    while True:
        print("")
        print("> Sua vez")
        print("")
        print("(A) Atacar")
        print("")
        print("(D) Defender")
        print("")
        print("(I) Usar Item")
        print("")
        op = input("Insira seu comando:").upper()
        if op in ["A", "D", "I"]:
            if op == "A":
                print("")
                print("Vez Inimigo")
                time.sleep(1)
                if random.randint(1,2) == 1:
                    print("")
                    print("Você Ataca e o Monstro Defende...")
                    valor_ataque = max(p1.forca - monstro.defesa, 0)
                    monstro.vida_atual = max(monstro.vida_atual - valor_ataque, 0)
                    print(f"Dano causado: {valor_ataque}")
                else:
                    print("")
                    print("Você e o Monstro Atacam...")
                    print("")
                    print(f"Dano causado: {p1.forca}")
                    print(f"Dano recebido: {monstro.forca}")
                    monstro.vida_atual = max(monstro.vida_atual - p1.forca, 0)
                    p1.vida_atual = max(p1.vida_atual - monstro.forca, 0)
                    
                
            if op == "D":
                print("")
                print("> Vez Inimigo")
                time.sleep(1)
                if random.randint(1,2) == 1:
                    print("")
                    print("Você e o Monstro Defendem...")
                    print("")
                    print("Nada Acontece...")
                else:
                    print("")
                    print("Você Defende e o Monstro Ataca...")
                    print("")
                    valor_ataque = max( monstro.forca - p1.defesa, 0)
                    p1.vida_atual = max(p1.vida_atual - valor_ataque, 0)
                    print(f"Dano recebido: {valor_ataque}")
            if op == "I":
                cli.interagir_item(p1)
                print("")
                print("Vez Inimigo")
                time.sleep(1)
                if random.randint(1,2) == 1:
                    print("")
                    print("Você usa a Mochila e o Monstro Defende...")
                    print("")
                    print("Nada Acontece...")
                else:
                    print("")
                    print("Você usa a Mochila e o Monstro Ataca...")
                    print("")
                    print(f"Dano recebido: {monstro.forca}")
                    p1.vida_atual = max(p1.vida_atual - monstro.forca,0)

            p1.ver_atributos()
            monstro.ver_atributos()



            vida_monstro = monstro.verifica_vida()
            vida_p1 = p1.verifica_vida()







            if not vida_monstro:
                print("")
                print("Você ganhou o Combate!")
                break

            if not vida_p1:
                print("")
                print("Monstro ganhou o Combate!")
                break
        else :print("Comando nao reconhecido")


