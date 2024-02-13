from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arqExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabecalho('\033[35mNOVO CADASTRO:\033[m')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do programa... Até logo!')
        break
    else:
        print('\033[31mERRO! Opção inserida é inválida!\033[m')
    sleep(2)

