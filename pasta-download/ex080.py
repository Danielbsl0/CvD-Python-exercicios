nums = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > nums[-1]:
        nums.append(n)
        print(f'O valor foi adicionado na última posição....')
    else:
        pos = 0
        while pos < len(nums):
            if n <= nums[pos]:
                nums.insert(pos, n)
                print(f'O valor foi adcionado na posição: {pos}.....')
                break
            pos += 1
print(f'Os valores digitados foram {nums}')
