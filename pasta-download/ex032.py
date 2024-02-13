ano = int(input('Insira o ano: '))
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if ano%4 == 0 and ano % 100 != 0 or ano%400 == 0:
    print(f'O ano escolhido foi \033[32m{ano}\033[m e ele é BISSEXTO')

else:
    print(f'O ano escolhido foi \033[31m{ano}\033[m e ele NÃO é bissexto')
print(f'{lin}')
