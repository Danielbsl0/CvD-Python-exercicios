from time import sleep
def cont(a, b, c):
    if c == 0:
        c += 1
    if b < a:
        if c > 0:
            print(f'Contagem de {a} até {b} de {c} em {c}')
            c *= -1
        else:
            print(f'Contagem de {a} até {b} de {c*-1} em {c*-1}')
        b -= 1
    else:
        print(f'Contagem de {a} até {b} de {c} em {c}')
        b += 1
    for c in range(a, b, c):
        sleep(1)
        print(f'{c}', end=' ')
    print('FIM!')


cont(1, 10, 1)
cont(10, 0, -2)
print('Agora é sua vez de personalizar!')
ini = int(input('ÍNICIO: '))
fim = int(input('FIM: '))
passo = int(input('PASSO: '))
cont(ini, fim, passo)
