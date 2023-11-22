tela = 40
def cria_divisao_texto(texto, inicio = "  ", meios = "  ", fim= "  "):
    steps = ((tela // 2) // len(meios)) - len(texto) // 2
    steps_inicio = steps - len(inicio)
    steps_fim = steps - len(fim)
    print()
    print(inicio + meios * steps_inicio  + texto + meios * steps_fim + fim)

def desenhar(p1, tesouro):
    cria_divisao_texto(" Mapa ","< ","~-"," >")
    for y in range(10):
        for x in range(10):
            if p1.posicao == [x,y]:
                print(" @ ", end="")
            elif tesouro.posicao == [x,y]:
                print(" X ", end="")
            else:
                print(" . ", end="")
        print("")



