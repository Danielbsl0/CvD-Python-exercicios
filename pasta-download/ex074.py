from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram', end=' ')
for c in n:
    print(f'{c}', end=' ')
print(f'\nO maior número sorteado foi {max(n)}\nO menor número sorteado foi {min(n)}')

