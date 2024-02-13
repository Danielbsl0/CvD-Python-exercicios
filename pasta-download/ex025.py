nome = str(input('Qual é o seu nome completo?:')).strip()
s = 'SILVA'
print(f'O nome possuí Silva?:\033[31m{s in nome.upper()}\033[m')



