def ficha(jog='<desconhecido>', gols=0):
    print(f'O jogador {jog} fez {gols} gol(s).')


nome = input('Digite o nome do jogador: ')
n = input('Digite quantos gols o jogador marcou: ')
if n == '':
    n = 0
    ficha(gols=n)
else:
    n = int(n)
    ficha(nome, n)
# Tá dando muito errado


