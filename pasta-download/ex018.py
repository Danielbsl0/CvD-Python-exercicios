from math import radians, sin, cos, tan
a = float(input('Qual é o valor do ângulo?:'))
sen = sin(radians(a))
co = cos(radians(a))
ta = tan(radians(a))
lin = 48*('\033[35m=\033[m')
print(f'{lin}')
print(f'O seno de \033[32m{a}°\033[m é igual a:\033[33m{sen:.3f}\033[m \nO cosseno é igual a:\033[34[m{co:.3f}\033[m \nE a tangente é igual a:\033[36m{ta:.3f}\033[m')
print(f'{lin}')