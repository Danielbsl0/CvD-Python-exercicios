n1 = float(input('Digite o número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite o último número: '))
menor = n1
maior = n1
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print(f'O menor número é:\033[31m{menor}\033[m\nO maior número é:\033[34m{maior}\033[m')
print(f'{lin}')


