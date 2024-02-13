l1 = float(input('Digite o primeiro lado: '))
l2 = float(input('Digite o segundo lado: '))
l3 = float(input('Digite o terceiro número: '))
lin = 64*('\033[35m=\033[m')
print (f'{lin}')
if l1< l2+l3 and l2<l1+l3 and l3<l1+l2 and l1!=l2!=l3:
    print('\033[32mPode formar um triângulo\033[m')
    print('O triângulo formado é um \033[36m ESCALENO\033[M')

elif l1< l2+l3 and l2<l1+l3 and l3<l1+l2 and l1 == l2 == l3:
    print('\033[32mPode formar um triângulo\033[m')
    print(f'O triângulo formado é um\033[33m EQUILÁTERO\033[m')

elif l1< l2+l3 and l2<l1+l3 and l3<l1+l2 and l1 == l2 or l1 == l3 or l2 == l3:
    print('\033[32mPode formar um triângulo\033[m')
    print(f'O triângulo formado é um\033[34m ISÓSCELES\033[m')

else:
    print('\033[31mNão pode formar um triângulo\033[m')
print(f'{lin}')