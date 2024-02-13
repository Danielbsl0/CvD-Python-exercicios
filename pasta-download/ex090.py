dados = dict()
dados['Nome'] = input('Nome: ')
dados['Média'] = float(input(f"Média de {dados['Nome']}: "))
if dados['Média'] >= 6:
    dados['Situação'] = 'APROVADO'
elif 7 > dados['Média'] >= 5:
    dados['Situação'] = 'RECUEPRAÇÃO'
else:
    dados['Situação'] = 'REPROVADO'
for k, v in dados.items():
    print(f'{k} é igual a {v}')
