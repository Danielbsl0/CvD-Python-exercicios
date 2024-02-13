from random import randint
from time import sleep
tot = 0
geral = []
jogos = []
lin = 24*'-='
print(lin)
print('JOGO DA MEGASENA')
print(lin)
quant = int(input('Quantos jogos você quer que eu sorteie?: '))
while tot <= quant:
    b = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            b += 1
        if b >= 6:
            break
    jogos.sort()
    geral.append(jogos[:])
    jogos.clear()
    tot += 1
print(5*'-=', f'SORTEANDO {quant} JOGOS...', 5*'-=')
sleep(3)
for i, p in enumerate(geral):
    print(f'Jogo{i}: {p}')


