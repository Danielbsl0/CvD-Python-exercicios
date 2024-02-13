def escreva(msg):
    print(len(msg)*'-' + 2*'-')
    print(f' {msg} ')
    print(len(msg)*'-' + 2*'-')


def manual():
    while True:
        escreva('\033[34mSISTEMA DE AJUDA PyHELP\033[m')
        comando = input('Função ou Biblioteca > ').strip().upper()
        if comando != 'FIM':
            escreva(f"Acessando o manual do comando '{comando}'")
            print(help(comando))
        else:
            escreva('\033[31mENCERRANDO O SISTEMA...\033[m')
            break


manual()
