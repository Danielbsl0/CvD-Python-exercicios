dados = []
while True:
    nome = input('NOME: ')
    nt1 = float(input('NOTA 1: '))
    nt2 = float(input('NOTA 2: '))
    perg = ' '
    md = (nt1+nt2)/2
    dados.append([nome, nt1, nt2, md])
    while perg not in 'SN':
        perg = input('Quer continuar? [S/N]: ').upper().strip()
    if perg == 'N':
        break
print(32*'-=')
print('Nº.   NOME      MÉDIA')
print(32*'-')
for i, p in enumerate(dados):
    print(f'{i:<4} {p[0]:<4} {p[3]:>6}')
    print()
while True:
    perg2 = (int(input('Mostrar notas de quais alunos?: (999 interrompe)')))
    if perg2 == 999:
        print('FIM DO PROGRAMA')
        break
    else:
        print(f'As notas dos alunos são: [{dados[perg2][1]}, {dados[perg2][2]}]')

