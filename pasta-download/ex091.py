from random import randint
from operator import itemgetter
players = dict()
players['jogador1'] = randint(0, 6)
players['jogador2'] = randint(0, 6)
players['jogador3'] = randint(0, 6)
players['jogador4'] = randint(0, 6)
ranking = list()
for k, v in players.items():
    print(f'O {k} tirou {v}')
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}ºlugar: {v[0]} com {v[1]} pontos')
