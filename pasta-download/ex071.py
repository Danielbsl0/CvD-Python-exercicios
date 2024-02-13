ced50 = ced20 = ced10 = ced1 = 0
while True:
    saque = int(input('Qual valor você deseja sacar: R$'))
    r1 = r2 = r3 = saque
    if saque >= 50:
        ced50 = int(saque/50)
        r1 = saque%50
    if saque >= 20:
        ced20 = int(r1/20)
        r2 = r1%20
    if saque >= 10:
        ced10 = int(r2/10)
        r3 = r2%10
    ced1 = int(r3/1)
    r4 = r3%1
    if ced50 >= 1:
        print(f'O número de cédulas de R$50 é:{ced50}')
    if ced20 >= 1:
        print(f'O número de cédulas de R$20 é:{ced20}')
    if ced10 >= 1:
        print(f'O número de cédulas de R$10 é:{ced10}')
    if ced1 >= 1:
        print(f'O número de cédulas de R$1 é:{ced1}')
    if r4 == 0:
        print('Muito obrigado por confiar nos serviços do BANCO BARBOSA!')
        break

