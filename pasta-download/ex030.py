n1 = int(input('Digite o número: '))
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if n1%2 ==0:
    print(f'O número escolhido foi:\033[31m{n1}\033[m, ele é par')

else:
    print(f'O número escolhido foi:\033[34m{n1}\033[m, ele é impar')
print(f'{lin}')

