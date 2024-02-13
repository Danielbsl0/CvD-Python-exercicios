import math
num = float(input('Digite um número:'))
n2 = math.floor(num)
lin = 64*('\033[33m=\033[m')
print(f'{lin}')
print(f'O número escolhido é \033[36m{num}\033[m, sua parte inteira é:\033[31m{n2}\033[m')
print(f'{lin}')
