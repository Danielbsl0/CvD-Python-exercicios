def voto(num):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ', end='')
    if idade >= 18 and idade <= 65:
        print('VOTA.')
    elif idade < 16:
        print('NÃO VOTA.')
    else:
        print('É OPCIONAL')


ano = int(input('Qual é o ano do seu nascimento?: '))
voto(ano)