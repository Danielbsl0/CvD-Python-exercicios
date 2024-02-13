c1 = c2 = c3 = 0
while True:
    idade = int(input('Digite a sua idade: '))
    sexo = ''
    perg = ''
    while sexo not in 'MF':
        sexo = str(input('Qual o seu sexo?(M/F):')).strip().upper()
    if idade > 18:
        c1 += 1
    if sexo == 'M':
        c2 += 1
    if idade > 20 and sexo == 'F':
        c3 += 1
    while perg not in 'SN':
        perg = str(input('Deseja continuar?(S/N): ')).strip().upper()
    if perg == 'N':
        break
print(f'A quantidade de pessoas com mais de 18 anos é {c1}, de homens cadastrados é {c2}', end=' ')
print(f'e a de mulheres com menos de 20 anos é {c3}')