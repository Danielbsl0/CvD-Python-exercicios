val = list()
for c in range(0, 5):
    val.append(int(input(f'Digite o valor na Posição {c}: ')))

print(f'O maior valor digitado foi {max(val)} nas posições: ', end='')
for i, v in enumerate(val):
    if v == max(val):
        print(f'{i,}', end=' ')
print(f'\nO menor valor digitado foi {min(val)} na posições: ', end='')
for i, v in enumerate(val):
    if v == min(val):
        print(f'{i,}', end=' ')




