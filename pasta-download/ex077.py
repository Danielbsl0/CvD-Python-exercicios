word = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
         'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
vogais = 'a', 'e', 'i', 'o', 'u'
for p in word:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(f'{letras}', end=' ')
            


