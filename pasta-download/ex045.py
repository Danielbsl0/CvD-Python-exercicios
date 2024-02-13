from random import randint
from time import sleep

joken = int(input('TABELA DE ESCOLHAS\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\n Escolha uma das opções: '))
pc = randint(1, 3)
p = str('PEDRA')
pp = str('PAPEL')
t = str('TESOURA')
print('\033[33mPROCESSANDO...\033[m')
sleep(3)

if joken == pc:
    print(f'O resultado é EMPATE')

elif joken == 1 and pc == 2:
    print(f'Foram escolhidos {p} e {pp} e o resultado é VITÓRIA do COMPUTADOR')

elif joken == 1 and pc == 3:
    print(f'Foram escolhidos {p} e {t} e o resultado é VITÓRIA do JOGADOR')

elif joken == 2 and pc == 1:
    print(f'Foram escolhidos {pp} e {p} e o resultado é VITÓRIA do JOGADOR')

elif joken == 2 and pc == 3:
    print(f'Foram escolhidos {pp} e {t} e o resultado é VITÓRIA do COMPUTADOR')

elif joken == 3 and pc == 1:
    print(f'Foram escolhidos {t} e {p} o resultado é VITÓRIA DO COMPUTADOR ')

else:
    print(f'Foram escolhidos {t} e {pp} o resultado é VITÓRIA do JOGADOR')
