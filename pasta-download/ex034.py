sal = float(input('Qual o seu sálario? '))
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if sal >1.250:
    buff = sal+(sal/100*10)
else:
    buff = sal+(sal/100*15)
print(f'O seu sálario atual é de R$\033[32m{sal}\033[m, com o seu aumento, ele sobe para:R$\033[36m{buff}\033[m')
print(f'{lin}')