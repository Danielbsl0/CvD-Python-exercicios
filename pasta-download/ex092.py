from datetime import date
dados = dict()
dados['nome'] = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
data = date.today().year
dados['idade'] = data - ano
dados['ctps'] = int(input('Carteira de Trabalho(0 não tem): '))
if dados['ctps'] >0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['aposentadoria'] = 35 - (data - dados['contratação']) + dados['idade']
print(32*'-=')
for i, k in dados.items():
    print(f'{i} tem o valor {k}')


