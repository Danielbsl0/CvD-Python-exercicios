num = int(input('Digite um valor: '))
mult = 0
lin = (48*'\033[35m=\033[m')
print(f'{lin}')
for cont in range(1, num +1):
    if num%cont == 0:
        print(f'É divisor desse número: \033[32m{cont}\033[m')
        mult += 1


if mult == 2:
    print('Esse número é PRIMO!!')
else:
    print('Esse número NÃO É PRIMO!!')
print(f'{lin}')