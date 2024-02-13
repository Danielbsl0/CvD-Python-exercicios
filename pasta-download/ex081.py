nums = []
while True:
    nums.append(int(input('Insira um número: ')))
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer continuar?(S/N): ').upper().strip()
    if perg == 'N':
        break
nums.sort(reverse=True)
print(f'Você digitou: \033[33m{len(nums)}\033[m elementos')
print(f'Os valores em ordem descrescente são: {nums}')
if 5 in nums:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')