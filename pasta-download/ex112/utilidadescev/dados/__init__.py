def leiaDinheiro(msg):
    ok = False
    while not ok:
        n = str(input(msg)).replace(',', '.').strip()

        if n.isalpha() or n == '':
            print(f'\033[31mERRO: "{n}" não é um preço válido!\033[m')
        else:
            ok = True
            return float(n)

