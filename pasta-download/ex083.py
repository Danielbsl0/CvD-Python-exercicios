perg = input('Digite uma expressão: ')
exp = list()
for simb in perg:
    if simb == '(':
        exp.append('(')
    if simb == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append('(')
if len(exp) == 0:
    print('A sua expressão é válida!')
else:
    print('A expressão é inválida!')
