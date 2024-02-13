dados = []
geral = []
maiorp = menorp = 0
nmaior = []
nmenor = []
while True:
    n = input('Digite seu nome: ')
    pes = float(input('Digite seu peso: '))
    dados.append(n)
    dados.append(pes)
    geral.append(dados[:])
    dados.clear()
    perg = ' '
    if len(geral) == 0:
        maiorp = pes
        menorp = pes
        nmaior.append(n)
        nmenor.append(n)
    else:
        if pes > maiorp:
            maiorp = pes
            nmaior.clear()
            nmaior.append(n)
        if pes == maiorp and n not in nmaior:
            nmaior.append(n)
        if pes < menorp:
            menorp = pes
            nmenor.clear()
            nmenor.append(n)
        if pes == menorp and n not in nmenor:
            nmenor.append(n)
    while perg not in 'SN':
        perg = input('Quer continuar(S/N)? ').upper().strip()
    if perg == 'N':
        break
print(f'Ao todo você cadastrou {len(geral)} pessoas')
print(f'O maior peso foi de {maiorp}Kg. Peso de {nmaior}')
print(f'O menor peso foi de {menorp}Kg. Peso de {nmenor}')
