nums = []
lin = 48*'-='
while True:
    n = int(input('Digite um valor: '))
    if n not in nums:
        print('Valor adicionado com sucesso....')
        nums.append(n)
    else:
        print('Valor já foi adicionado, portanto não adicionarei de novo.....')
    perg = input('Quer continuar?(S/N): ').upper().strip()
    while perg not in 'SN':
        perg = input('Quer continuar?(S/N): ').upper().strip()
    if perg in 'N':
        print(f'{lin}\nVocê digitou os valores {sorted(nums)}')
        break

