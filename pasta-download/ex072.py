seq = 'Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte'
while True:
    n1 = int(input('Digite um número entre 0 e 20: '))
    if 20 >= n1 >= 0:
        break
    print('Tente novamente. ', end='')
print(f'O número escolhido foi {seq[n1]}')