from random import randint
from time import sleep
print('Eu escolhi um número entre 1 e 5')
num1 = randint(0, 5)
num2 = int(input('Qual foi o número que eu pensei?: '))
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if num2 == num1:
    print(f'Parabéns, você acertou, o número era \033[31m{num1}\033[m')

else:
    print(f'Infelizmente o número não era esse, a resposta certa era \033[32m{num1}\033[m')
print(f'{lin}')
