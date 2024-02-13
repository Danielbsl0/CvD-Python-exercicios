from random import shuffle
n1 = str(input('Digite o nome do aluno:'))
n2 = str(input('Digite o nome do segundo:'))
n3 = str(input('Digite o nome do terceiro'))
n4 = str(input('Digite o nome do último'))
lista =[n1, n2, n3, n4]
shuffle(lista)
print('A sequência escolhida para a apresentação é: ')
print(f'\033[31m{lista}\033[m')
