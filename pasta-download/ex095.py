dados = dict()
rounds = list()
geral = list()
while True:
    dados.clear()
    dados['nome'] = input('Nome: ')
    part = int(input(f"Quantas partidas {dados['nome']} jogou?: "))
    rounds.clear()
    for c in range(part):
        rounds.append(int(input(f'Quantos gols na partida {c+1}?: ')))
    dados['gols'] = rounds[:]
    dados['total'] = sum(rounds)
    perg = ' '
    geral.append(dados.copy())
    while perg not in 'SN':
        perg = input('Quer continuar?(S/N): ').upper().strip()[0]
    if perg == 'N':
        break
print('cod ', end='')
for c in dados.keys():
    print(f'{c:>15}', end='')
print()
print(32*'-')
for i, v in enumerate(geral):
    print(f'{i:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(32*'-')
while True:
    perg2 = int(input('Mostrar dados de qual jogador?(999 PARA PARAR): '))
    if perg2 == 999:
        break
    if perg2 >= len(geral):
        print(f'ERRO! NÃO EXISTE JOGADOR CÓDIGO {perg2}')
    else:
        print(f"LEVANTAMENTO DO JOGADOR {geral[perg2]['nome']}")
        for k, v in enumerate(geral[perg2]['gols']):
            print(f'    =>Na partida {k+1}, fez {v} gols.')
