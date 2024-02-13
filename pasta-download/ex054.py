from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for c in range(0, 7):
    ano = int(input('Qual é o ano em que você nasceu?: '))
    idade = atual-ano
    print(f'Essa pessoa tem \033[33m{idade}\033[m anos')
    if idade >= 21:
        print('Essa pessoa atingiu a \033[32mMAIORIDADE\033[m')
        cont += 1
    else:
        print('Essa pessoa \033[31mNÃO\33[m atingiu a maioridade')
        cont2 += 1
print(f'O número de pessoas que atingiu a maioridade é: \033[34m{cont}\033[m e de quem não atingiu é: \033[35m{cont2}\033[m')
