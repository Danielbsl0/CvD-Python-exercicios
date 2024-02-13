dist = float(input('Qual a distância? '))
lin = ('\033[35m=\033[m')
if dist<=200:
    val = 0.50*dist
    print(f'Para uma viagem de \033[31m{dist}Km\033[m, o custo é de: R$\033[32m{val}\033[m')

else:
    val = 0.45*dist
    print(f'Para uma viagem de \033[31m{dist}Km\033[m, como é de mais longa, o custo será de apenas: R$\033[32m{val}\033[m')


