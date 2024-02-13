dados = []
pessoa = dict()
idade = []
mul = []
maiormedia = []
while True:
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = ' '
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = input('Sexo[M/F]: ').strip().upper()[0]
    if pessoa['sexo'] == 'F':
        mul.append(pessoa['nome'])
    pessoa['idade'] = int(input('Idade: '))
    idade.append(pessoa['idade'])
    dados.append(pessoa.copy())
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer continuar(S/N)?: ').upper().strip()[0]
    if perg == 'N':
        break
media = sum(idade) / len(dados)
print(f'- Ao todo temos {len(dados)} pessoas cadastradas.')
print(f'- A média de idade é {media:.2f} anos')
print(f'- As mulheres cadastradas foram: {mul}')
print(f'- Lista de pessoas acima da média: \n')
if pessoa['idade'] > media:
    maiormedia.append(pessoa.copy())
for p, v in enumerate(maiormedia):
    print(v)
