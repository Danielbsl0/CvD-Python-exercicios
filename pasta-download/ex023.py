n1 = int(input('Digite um número:'))
un = n1//1%10
dez = n1//10%10
cen = n1//100%10
mil = n1//1000%10
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
print(f'O número escolhido é:\033[31m{n1}\033[m')
print(f'Sua unidade é:\033[32m{un}\033[m')
print(f'Sua dezena é:\033[33m{dez}\033[m')
print(f'Sua centena é:\033[34m{cen}\033[m')
print(f'Seu milhar é:\033[36m{mil}\033[m')
print(f'{lin}')
