def leiaint(msg):
    ok = False
    n = 0
    while True:
        try:
            n = int(input(msg))
            ok = True
        except Exception as erro:
            print(f'\033[31mERRO! INSIRA UM VALOR NÚMERICO VÁLIDO!\033[m')
        if ok:
            break
    return n


n = leiaint('Digite um valor inteiro: ')
print(f'O valor inserido foi o {n}')
