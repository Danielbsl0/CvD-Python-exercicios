n1 = int(input('Digite um número:'))
n2 = n1 * 2
n3 = n1 * 3
n4 = n1**(1/2)
lin = 42*'\033[31m=\033[m'
print(f'{lin}')
print(f'O número escolhido foi:\033[34m{n1}\033[m, \nO dobro é:\033[35m{n2}\033[m, \nO triplo é:\033[36m{n3}\033[m \nE a raiz quadrada dele é: \033[37m{n4}\033[m')
print(f'{lin}')

