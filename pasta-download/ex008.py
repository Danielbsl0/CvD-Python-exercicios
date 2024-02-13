und = float(input('Digite um valor em metros:'))
cm = und*100
mm = cm*1000
lin = 40*'\033[31m=\033[m'
print(f'{lin}')
print(f'Você digitou \033[33m{und}m\033[m, \n\033[33m{und}m\033[m possuí \033[34m{cm}cm\033[m e \033[32m{mm}mm\033[m')
print(f'{lin}')