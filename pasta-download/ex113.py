def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except Exception as erro:
            print(f'\033[31mERRO! INSIRA UM VALOR NÚMERICO VÁLIDO!\033[m')
            continue
        else:
            return n


def leiaFloat(msg):
    while True:
       try:
           n2 = float(input(msg))
       except Exception as erro:
           print(f'\033[31mERRO! INSIRA UM VALOR VÁLIDO!\033[m')
       else:
           return n2

n = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'O valor inteiro inserido foi o {n}, já o valor real inserido foi {n2}')

