peso = float(input('Qual o seu peso?: '))
altura = float(input('Qual a sua altura?: '))
imc = peso / (altura**2)
lin = 48*('\033[35m=\033[m')
print(f'{lin}')
if imc < 18.5:
    print('Você está \033[34mABAIXO\033[m do peso.')

elif imc <25:
    print('Você está no peso \033[32mIDEAL\033[m.')

elif imc <30:
    print('Você está \033[36mSOBREPESO\033[m.')

elif imc <=40:
    print('Você está \033[33mOBESO\033[m.')

else:
    print('Você está com \033[31mOBESIDADE MÓRBIDA\033[M')
print(f'{lin}')