n = input('Digite algo:')
lin = 32*'\033[33m=\033[m'
print(f'{lin}\nO tipo do valor é:\033[31m', type(n), '\033[m')
print('Só tem espaços?\033[32m', n.isspace(), '\033[m')
print('Está capitalizada?\033[33m', n.istitle(), '\033[m')
print('É um número?\033[34m', n.isnumeric(), '\033[m')
print('É uma palavra?\033[35m', n.isalpha(), '\033[m')
print('É alfanumérico?\033[36m', n.isalnum(), '\033[m')
print('Está em maiúsculo?\033[37m', n.isupper(), '\033[m')
print('Está em minúsculo?\033[30m', n.islower(), '\033[m')
print(f'{lin}')

