c = float(input('Quantos graus está agora?:'))
f = c*9/5 + 32
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
print(f'A temperatura atual é de: \033[32m{c}\033[mºC. \nConvertido para ºF é igual a:\033[33m{f}\033[mºF')
print(f'{lin}')
