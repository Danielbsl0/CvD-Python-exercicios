dados = dict()
dados['nome'] = input('Nome: ')
part = int(input(f"Quantas partidas {dados['nome']} jogou?: "))
dados['gols'] = []
cont = 0
for c in range(part):
    gol = int(input(f'Quantos gols na partida {c+1}?: '))
    dados['gols'].append(gol)
    cont += gol
dados['total'] = cont
print(32*'-=')
print(dados)
print(32*'-=')
for i, k in dados.items():
    print(f'O campo {i} tem o valor: {k}.')
print(32*'-=')
print(f"O jogador {dados['nome']} jogou {part} partidas.")
for k, v in enumerate(dados['gols']):
    print(f'    =>Na partida {k}, fez {v} gols.')
print(f"Foi um total de {dados['total']} gols.")
