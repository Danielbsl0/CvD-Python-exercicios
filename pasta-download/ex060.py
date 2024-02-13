n1 = int(input('Digite um número para que seja calculado o seu fatorial'))
c1 = n1
f1 = 1
print(f'Calculando {n1}! = ', end='')
while c1 > 0:
    print(f'{c1} ', end='')
    print('X ' if c1 > 1 else '= ', end=f'')
    f1 *= c1
    c1 -= 1
print(f'{f1}')
print(f'O fatorial de {n1} é {f1}!')