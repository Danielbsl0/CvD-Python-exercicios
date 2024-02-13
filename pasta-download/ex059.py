n1 = float(input('Digite o primeiro valor'))
n2 = float(input('Digite o segundo valor '))
print(f'''MENU:
[1]somar
[2]multiplicar 
[3]maior
[4]novos números
[5]sair do programa''')
men = int(input('Digite um valor: '))
while men != 5:
    if men == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é: {soma}!')
        print(f'''MENU:
        [1]somar
        [2]multiplicar 
        [3]maior
        [4]novos números
        [5]sair do programa''')
        men = int(input('Digite um valor: '))
    elif men == 2:
        prod = n1*n2
        print(f'O produto dos números {n1} e {n2} é: {prod}!')
        print(f'''MENU:
        [1]somar
        [2]multiplicar 
        [3]maior
        [4]novos números
        [5]sair do programa''')
        men = int(input('Digite um valor: '))
    elif men == 3:
        if n1>n2:
            maior = n1
            print(f'O maior valor entre os números é {maior}')
        elif n2>n1:
            maior = n2
            print(f'O maior valor entre os números é {maior}')
        else:
            print('Ambos os valores são iguais :)')
        print(f'''MENU:
        [1]somar
        [2]multiplicar 
        [3]maior
        [4]novos números
        [5]sair do programa''')
        men = int(input('Digite um valor: '))
    elif men == 4:
        n1 = float(input('Digite o primeiro valor'))
        n2 = float(input('Digite o segundo valor '))
        print(f'''MENU:
        [1]somar
        [2]multiplicar 
        [3]maior
        [4]novos números
        [5]sair do programa''')
        men = int(input('Digite um valor: '))
print('\033[32mFIM DO PROGRAMA\033[m')
