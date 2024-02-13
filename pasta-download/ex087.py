mat = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
cc1 = cc2 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if mat[l][c] % 2 == 0:
            cc1 += mat[l][c]
        if c == 2:
            cc2 += mat[l][c]
        if l == 1:
            if c == 0:
                maior = mat[l][c]
            else:
                if mat[l][c] > maior:
                    maior = mat[l][c]
print(32*'-=')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
print(32*'-=')
print(f'A soma dos valores pares é {cc1}\nA soma dos valores da terceira coluna é {cc2}\nO maior valor da segunda linha é: {maior}')
