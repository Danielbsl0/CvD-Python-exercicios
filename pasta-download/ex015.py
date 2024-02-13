s = float(input('Quantos Km foram rodados?:'))
t = int(input('Quantos dias o carro foi alugado?'))
val = 0.15*s + 60*t
lin = 48*('\033[35m=\033[m')
print(f'{lin}')
print(f'O valor a ser pago por:\033[32m{s}\033[mKm \ne por \033[33m{t}\033[m dias com o carro \né de: R$\033[1;34m{val:.2f}\033[m')
print(f'{lin}')
