from random import randint
from time import sleep
c = 1
print('Eu escolhi um número entre 1 e 5')
num1 = randint(0, 5)
num2 = int(input('Qual foi o número que eu pensei?: '))
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
while num2 != num1:
    print('\033[33mPROCESSANDO...\033[m')
    sleep(3)
    print(f'Infelizmente o número não era {num2}, vamos tentar novamente')
    num2 = int(input('Qual foi o número que eu pensei?: '))
    c += 1
print('\033[33mPROCESSANDO...\033[m')
sleep(3)
print(f'Parabéns você acertou! Foram necessesárias \033[34m{c}\033[m tentativas para isso!')
print(f'{lin}')
