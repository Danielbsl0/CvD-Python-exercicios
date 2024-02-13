def metade(n=0, opc=False):
    if opc==True:
        return moeda(n/2)
    return n/2

def dobro(n=0, opc=False):
    if opc==True:
        return moeda(n*2)
    else:
        return n*2


def aumentar(n=0, mais=0, opc=False):
    if opc==True:
        return moeda(n + (n/100)*mais)
    else:
        return n + (n/100)*mais


def diminuir(n=0, menos=0, opc=False):
    if opc==True:
        return moeda(n - (n/100)*menos)
    else:
        return n - (n/100)*menos


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


def resumo(n=0, mais=0, menos=0):
    print(32*'-')
    print(f'RESUMO DO VALOR'.center(30))
    print(32*'-')
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{mais}% de aumento: \t{aumentar(n, mais, True)}')
    print(f'{menos}% de aumento: \t{diminuir(n, menos, True)}')
    print(32*'-')
