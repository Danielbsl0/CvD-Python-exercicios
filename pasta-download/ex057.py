sexo = str(input('Qual é o seu sexo?(M/F): ')).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input('Qual é o seu sexo?(M/F): ')).upper().strip()[0]
if sexo == "M":
    print(f'Sexo {sexo} registrado')
else:
    print(f'Sexo {sexo} registrado')
