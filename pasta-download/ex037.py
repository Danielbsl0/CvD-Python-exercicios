n1 = int(input('Digite um número inteiro qualquer:'))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção é: '))
if opção == 1:
    print(f'{n1} convertido para BINÁRIO é igual a {bin(n1)}')
elif opção == 2:
    print(f'{n1} convertido para OCTAL é igual a {oct(n1)}')
elif opção == 3:
    print(f'{n1} convertido para HEXADECIMAL é igual a {hex(n1)}')
else:
    print(f'Opção inválida, tente novamente')

