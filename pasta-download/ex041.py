ano = int(input('Qual é o ano do seu nascimento?: '))
idade = 2023-ano
lin = 64*('\033[1;35m=\033[m')
print(f'{lin}')

if idade <= 9:
    print(f'Você nasceu em \033[31m{ano}\033[m, logo sua categoria é MIRIM')

elif idade <= 14:
    print(f'Você nasceu em \033[32m{ano}\033[m, logo sua categoria é INFANTIL')

elif idade <= 19:
    print(f'Você nasceu em \033[33m{ano}\033[m, logo sua categoria é JUNIOR')

elif idade == 20:
    print(f'Você nasceu em \033[34m{ano}\033[m, logo sua categoria é SÊNIOR')

else:
    print(f'Você nasceu em \033[36m{ano}\033[m, logo sua categoria é MASTER')
print(f'{lin}')