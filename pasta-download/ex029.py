vel = float(input('Qual a velocidade do carro?: '))
lin = 64*('\033[33m=\033[m')
print(f'{lin}')
if vel> 80:
    print(f'Oh não! Você foi multado, o limite permitido é \033[32m{vel}Km/h\033[m')
    multa = (vel-80)*7
    print(f'Você deve pagar: R$\033[31m{multa}\033[m')

else:
    print(f'Muito bem! Você está dentro do limite de velocidade')

print(f'Tenha um bom dia, dirija com segurança')
print(f'{lin}')


