din = float(input('Qual é o seu orçamento? R$'))
dol = din/3.27
lin = 72*('\033[35m=\033[m')
print(f'{lin}')
print(f'Seu orçamento atual é de: R$\033[32m{din}\033[m. Com isso é possível comprar US$\033[31m{dol:.3f}\033[m')
print(f'{lin}')
