mat = [[], [], []]
cc1 = cc2 = 0
for c in range(0, 9):
    perg = int(input(f'Digite um valor para [{cc1}, {cc2}]:'))
    if cc2 < 2:
        cc2 += 1
    else:
        cc2 = 0
        cc1 += 1
    if c < 3:
        mat[0].append(perg)
    elif c < 6:
        mat[1].append(perg)
    elif c < 9:
        mat[2].append(perg)
print(32*'-=')
for p in mat:
    print(f'[   {p[0]}   ] [   {p[1]}   ] [    {p[2]}    ]', end=' ')
    print()

