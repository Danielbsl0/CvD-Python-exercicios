from random import randint
from time import sleep
numeros = []
def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Sorteando 5 valores da lista: ', end=' ')
    for val in numeros:
        print(f'{val}', end=' ', flush=True)
        sleep(0.5)
    print(f'PRONTO!')
def somapar():
    spar = 0
    for val in numeros:
        if val % 2 == 0:
            spar += val
    print(f'Somando os valores pares de {numeros}, temos ', end='', flush=True)
    sleep(0.5)
    print(spar)


sorteia()
somapar()

            