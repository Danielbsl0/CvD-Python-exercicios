from time import sleep

def maior(* num):
    tam = len(num)
    print(f'Analisando os valores passados....')
    sleep(1)
    maior = 0
    for i, val in enumerate(num):
        print(f'{val}', end= ' ', flush=True)
        sleep(0.5)
        if i == 0:
            maior == val
        else:
            if maior < val:
                maior = val
        if tam == 0:
            maior = 0
    print(f'Foram informados {tam} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print(32*'-=')
print(32*'-=')
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
