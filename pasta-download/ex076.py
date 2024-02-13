lista = ('Lápis', 1, 'Caneta', 1.50, 'Borracha', 2 , 'Caderno', 15.90,
         'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
lin = 48*'-'
tit = 'LISTAGEM DE PREÇOS'
print(lin)
print(f'{tit:^48}')
print(lin)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print(lin)