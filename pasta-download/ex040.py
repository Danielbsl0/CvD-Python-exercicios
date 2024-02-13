nt1 = float(input('Qual foi a primeira nota?: '))
nt2 = float(input('Qual foi a segunda nota?: '))
md = (nt1 + nt2)/2
if md <5.0:
    print(f'Oh não!! Sua média é {md}, você foi reprovado :(')

elif md >=5.0 and md<6.9:
    print(f'Eita, sua média é {md}, você está de recuperação!')

else:
    print(f'Parabéns!! Sua média é {md}, você está APROVADO :)')
