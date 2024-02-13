n = s = c = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Ao todo foram digitados {c} números e soma de todos os números é: {s}')