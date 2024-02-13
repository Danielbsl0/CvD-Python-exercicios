perg = 'S'
c1 = 0
c2 = 0
maior = 0
menor = 0
n1 = 0
while perg not in "Nn":
    n1 = int(input('Digite 1 número:'))
    c1 += n1
    c2 += 1
    perg = str(input('Quer continuar? [S/N]'))
    if c2 == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1

print(f'A média entre os valores digitados é {c1/c2}', end=' ')
print(f'e o maior valor digitado foi: {maior}, e o menor foi: {menor}')
