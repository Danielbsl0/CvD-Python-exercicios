n1 = int(input('Digite 999 para parar: '))
c1 = n1
c2 = 0
while n1 != 999:
    n1 = int(input('Digite 999 para parar: '))
    c1 += n1
    c2 += 1

print(f'A quantidade de números digitados foi: {c2} e o valor da soma de todos esses valores é: {c1 - 999}')
