nome = input('Qual é o nome do aluno?:')
nt1 = float(input('Digite a nota do primeiro semestre:'))
nt2 = float(input('Digite a nota do segundo semestre:'))
md = (nt1 + nt2)/2
lin = 40*'\033[33m=\033[m'
print(f'{lin}')
print(f'Olá \033[36m{nome}\033[m! \nA sua nota do primeiro bimestre foi:\033[31m{nt1}\033[m. \nA sua nota do segundo bimestre foi:\033[34m{nt2}\033[m.')
print(f'Portanto a sua média é:\033[35m{md}\033[m')
print(f'{lin}')