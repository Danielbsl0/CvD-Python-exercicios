from math import hypot
n1 = float(input('Digite o cateto oposto:'))
n2 = float(input('Digite o cateto adjacente:'))
hip = hypot(n1, n2)
lin = 84*('\033[33m=\033[m')
print(f'{lin}')
print(f'A hipotenusa de um triângulo retângulo cujo tem como catetos:\033[31m{n1}\033[m e \033[34m{n2}\033[m, é igual a:\033[35m{hip:.2f}\033[m')
print(f'{lin}')

