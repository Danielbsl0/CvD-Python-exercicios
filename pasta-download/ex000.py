frase = 'Curso em Vídeo Python'
print(frase[0:21:2]) #Vai printar do 0 até o 21 caractere pulando de 2 em 2
print(frase[:5]) #Vai começar antes do dois pontos, ou seja, do início, já que não há nada escrito
print(frase[15:]) #Vai começar do 15 até o final
print(frase[9::3]) #entre o os dois pontos não há nada, então vai contar do 9 até o final pulando em 3 em 3
print(len(frase)) #Vai mostrar o comprimento da string
print(frase.count('a')) #Vai contar quantas vezes aparece a letra na frase (diferencia A de a)
print(frase.count('o',15,80)) #Vai mostrar quantos "o" tem entre a 15º letra e a última
print(frase.find('Python')) #Vai mostrar de onde começou a sequência de string
print('Curso'in frase) #Existe "Curso" em frase? True ou False
print(frase.replace('Python', 'Android')) #Irá substituir "Python" por "Android"
print(frase.upper()) #Deixará toda a frase em caixa alta
print(frase.lower()) #Deixará toda a frase em letras minúsculas
print(frase.capitalize()) #Todas as letras ficrão em letra minúscula, e a primeira ficará em caixa alta
print(frase.title()) #As primeiras letras de cada palavra ficarão em maiúsculas
print('frase:>7f') #Alinhar a direita
print('frase:<7f') #Alinhar a esquerda
print('frase:^7f') #Alinhar ao centro
frase2 = '   Aprenda Python   '
print(frase2.strip()) #Vai remover todos os espaços inúteis antes e depois da string
print(frase2.rstrip()) #Removerá os espaços inúteis a direita
print(frase2.lstrip()) #Removerá os espaços inúteis a esquerda
print(frase.split()) #Onde houver espaços o split fará uma divisão
dividido = frase.split()
print(dividido[2][3])
print(''.join(frase.split()))
print(frase[::-1]) #Vai escrever ao contrário
if 'Curso' in frase:
    print('YES')
else:
    print('NO')
frase_invertida = frase[::-1]
print(frase_invertida)
n = s = 0
while True: #Enquanto ETERNO
    n = int(input('Digite um valor'))
    if n == 999:
        break#PARA INTERROMPER UMA REPETIÇÃO
    s += n
print(f'A soma dos números digitados é {s}')
#LISTAS:
#usando listas []
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.insert(2, 2) #Na posição 2, inserir 2
if 4 in num:
    num.remove(4)
else:
    print('Não achei o valor 5')
#num.pop(2)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
print(valores)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei {v}!')
for c in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
a = [2, 3 , 4 , 7]
b = a #Igualando
b = a[:] #Cópia
b[2] = 8
print(f'Lista A: {a}\nLista B: {b}')
max or min #Funções para maior valor ou menor valor
dados = dict()
dados2 = {'nome': 'Pedro', 'idade': 25}
print(dados['nome'])
dados['sexo'] = 'M'
del dados['idade']
filme = {'titulo: '}
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = input('Qual o nome do estado?: ')
    estado['sigla'] = input('Qual a sigla?: ')
    brasil.append(estado.copy())
print(brasil)
#key=itemgetter(1)
#sum(partidas)  Para somar items em uma lista
def lin():
    print(32*'-')
def titulo(txt):
    print(30*'-')
    print(txt)
    print(30*'-')
titulo('   CURSO EM VÍDEO    ')
titulo('   PYTHON 3   ')
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)


soma(b=4, a=5)
def contador(*num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


contador(1, 2 , 3)
contador(2, 3)
contador(3, 5, 7, 9)
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 7, 8, 5, 4]
dobra(valores)
print(valores)
def voto():
    help()
    print(input.__doc__)
    def teste(b):
        global a
        a = 8
        b += 4
        c = 2
        print(f'A dentro é {a}')
        print(f'B dentro é {b}')
        print(f'C dentro é {c}')


    a = 5
    teste(a)
    print(f'A fora é {a}')
    def soma(a=0 , b=0 , c=0):
        s = a + b + c
        return s


    r1 = soma(1, 2, 3)
    r2 = soma(2, 5, 4)
    r3 = soma(2, 4 , 6)
    print(f'Os resultados foram {r1}, {r2}, {r3}')
    def fatorial(num=1):
        f = 1
        for c in range(num, 0, -1):
            f *= c
        return f

    n = int(input('Digite um número: '))
    print(f'O fatorial de {n} é {fatorial(n)}')
    def par(n=0):
        if n % 2 == 0:
            return True
        else:
            return False

    num = int(input('Digite um número: '))
    if par(num):
        print('É par')
    else:
        print('Não é par')
g.isnumeric() # Saber se é númerico
from uteis import numeros
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é: {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
f'\t' #tabulação
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except Exception as erro: # Um mesmo try pode ter vários exceptions
    print(f'O problema encontrado foi {erro.__class__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, muito obrigado :)')
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except (KeyboardInterrupt):
    print(f'O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado é {r:.2f}')
finally:
    print('Volte sempre, muito obrigado :)')