ano = int(input('Em que ano você nasceu?'))
idade = 2023-ano

if idade == 18:
    print('Parece que está na hora de você se alistar ao exército!')

elif idade <= 18:
    print(f'Você ainda vai se alistar ao exército, faltam \033[32m{18-idade}\033[m anos para isso!')

else:
    print(f'Já se passaram \033[31m{idade-18}\033[m anos do seu prazo para alistamento no exército!')
