#Tá errado, só funciona a contagem de mulheres, boa sorte :)
media = 0
cont = 0
man = 0
for c in range(0, 4):
    nome = str(input('Qual seu nome?: '))
    idade = int(input('Quantos anos você tem?: '))
    sex = int(input('''HOMEM = 1
MULHER = 2
Escolha uma das opções: '''))
    media = sum(c)/4
    if idade <= 20 and sex == 2:
        cont += 1
    if sex == 1 and c == 0 or c == 1 or 0 == 2 or 0 == 3:
        vel = idade
    else:
        if idade > vel:
           man = nome

print(f'A média de idade dessas pessoas é {media}, já o nome do homem mais velho é {vel} e por último a quantidade de mulheres com menos de 20 anos é: {cont}')
