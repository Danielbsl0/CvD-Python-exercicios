c1 = c2 = c3 = menor = 0
barato = ''
while True:
    nome = str(input('NOME: '))
    preco = float(input('PREÇO:R$ '))
    c1 += preco
    c3 += 1
    if c3 == 1 or preco < menor:
        menor = preco
        barato = nome

    if preco > 1000:
        c2 += 1

    if preco < c3:
        c3 = preco
        menor = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?(S/N): ')).upper().strip()
    if resp == 'N':
        break
print(f'O total gasto da compra é de R${c1}\nNo total há {c2} produtos que custam mais que R$1000,00')
print(f'O nome do produto mais barato é {barato}')
