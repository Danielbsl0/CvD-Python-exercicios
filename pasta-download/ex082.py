nums1 = []
nums2 = []
nums3 = []
while True:
    n = int(input('Digite um número: '))
    perg = ' '
    while perg not in 'SN':
        perg = input('Quer continuar?(S/N): ').upper().strip()
    if perg == 'N':
        break
    nums1.append(n)
    if n % 2 == 0:
        nums2.append(n)
    else:
        nums3.append(n)
print(f'Os valores adicionados foram: {nums1}')
print(f'Desses, os pares são: {nums2}')
print(f'E os ímpares são: {nums3}')