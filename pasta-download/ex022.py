frase = str(input('Digite o seu nome completo:')).strip()
le = len(frase) - frase.count(' ')
f = frase.find(' ')
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
print(f'Seu nome em maiúsculas é: \033[1;31m{frase.upper()}\033[m')
print(f'Seu nome em minúsculo é: \033[1;32m{frase.lower()}\033[m')
print(f'Seu nome contém \033[33m{le}\033[m letras')
print(f'Seu primeiro nome contém \033[34m{f}\033[m letras')
print(f'{lin}')


