val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário?: '))
ano = int(input('Por quantos anos você vai pagar o empréstimo?'))
prest = val/ano*12
lin = 64*('\033[35m=\033[m')
print(f'{lin}')
if prest<=sal*30/100:
    print(f'Seu empréstimo foi aprovado, o valor da prestação é: R$\033[32m{prest}\033[m')

else:
    print(f'Ooops! A sua prestação é maior que 30% do seu salário, logo o empréstimo foi negado :(')
print(f'{lin}')