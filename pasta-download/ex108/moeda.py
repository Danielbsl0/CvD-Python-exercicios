def metade(n=0):
    return n/2


def dobro(n=0):
    return n*2


def aumentar(n=0, mais=0):
    return n + (n/100)*mais


def diminuir(n=0, menos=0):
    return n - (n/100)*menos


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')


