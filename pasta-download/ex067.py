#Ta dando ERRADO :)
while True:
    n1 = int(input('Qual valor você quer ver a tabuada?: '))
    c = 0
    prod = 0
    while c != 10 and n1 >= 0:
        c += 1
        prod = c * n1
        print(f'{n1} X {c} = {prod}')
    if n1 <0:
        break
print('PROGRAMA DE TABUADA ENCERRADO.VOLTE SEMPRE')


