txt = str(input('Digite uma frase: ')).strip().upper()
invtd = txt[::-1].strip()
j1 = ''.join(txt.split())
j2 = ''.join(invtd.split())
lin = 48*('\033[35m=\033[m')
print(lin)
print(f'O inverso de \033[34m{j1}\033[m é: \033[33m{j2}\033[m')
if invtd[::-1] == txt:
    print('Essa frase é um \033[32mPALÍNDROMO\033[m!')
else:
    print('Essa frase \033[31mNÃO\033[m é um palíndromo')
print(lin)