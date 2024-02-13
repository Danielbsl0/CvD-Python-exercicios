maior = 0
menor = 0
for c in range(0, 5):
    pes = float(input('Digite o peso da pessoa: '))
    if c == 0:
        maior = pes
        menor = pes
    else:
        if pes > maior:
            maior = pes
        if pes < menor:
            menor = pes
print(f'O maior peso é: {maior} e o menor: {menor}')

