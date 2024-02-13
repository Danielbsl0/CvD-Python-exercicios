from time import sleep
from random import randint
v = 0
while True:
    n1 = int(input('Digite um valor: '))
    n2 = randint(1, 10)
    soma = n1 + n2
    jogo = ' '
    while jogo not in 'PI':
        jogo = str(input('PAR OU ÍMPAR?(P/I): ')).strip().upper()[0]
    print(f'Você jogou {n1} e o computador {n2}. Total de {soma}', end=' ')
    print(f'DEU PAR' if soma%2 == 0 else 'DEU ÍMPAR')
    if jogo == "P":
        if soma % 2 == 0:
            print(f'O USUÁRIO VENCEU')
            v += 1
        else:
            print(f'O COMPUTADOR VENCEU')
            break
    elif jogo == 'I':
        if soma%2 == 1:
            print(f'O USUÁRIO VENCEU')
            v += 1
        else:
            print(f'O COMPUTADOR VENCEU')
            break
    print(f'Vamos jogar novamente.....')
    sleep(3)
print(f'Fim de jogo, você venceu {v} vezes')
