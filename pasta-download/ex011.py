b = float(input('Qual é a largura da parede em metros?'))
h = float(input('Qual é a altura dela em metros?'))
a = b * h
tint = a/2
lin = 66*('\033[35m=\033[m')
print(f'{lin}')
print(f'A parede escolhida possúi uma largura de:\033[31m{b}\033[mm e a altura de:\033[32m{h}\033[mm.')
print(f'Sua área corresponde a:\033[33m{a:.2f}\033[mm². \n Portanto para se pintar esta parede é necessário \033[1;34m{tint:.2f}\033[mL')
print(f'{lin}')
