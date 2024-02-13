num = int(input('Digite o primeiro termo: '))
raz = int(input('Em uma PA, qual a razão entre os números?'))
c = 0
while c != 10:
    print(num+raz*c)
    c += 1
termo = int(input('Você quer mostrar mais quantos termos? '))
while termo != 0:
    c2 = c + termo
    while c < c2:
        print(num+raz*c)
        c += 1
    termo = int(input('Você quer mostrar mais quantos termos? '))
print(f'\033[32mFIM DO PROGRAMA\033[m')
