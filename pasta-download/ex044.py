preço = float(input('Qual o valor do produto?: R$'))
pag = int(input('FORMAS DE PAGAMENTO\n[1] dinheiro/cheque \n[2] cartão a vista\n[3] até 2x no cartão\n[4] 3x ou mais no cartão\nQual a condição de pagamento?: '))

if pag == 1:
    val = preço - (preço*10)/100
    print(f'O valor a ser pago é de R${val}, com desconto de {preço-val}')

elif pag == 2:
    val = preço - (preço*5)/100
    print(f'O valor a ser pago é de R${val}, com o desconto de {preço-val}')

elif pag == 3:
    val = preço
    print(f'O valor a ser pago é de R${val}')

else:
    val = preço + (preço*20)/100
    print(f'O valor a ser pago é de R${val}, com o acréscimo de {val-preço}')



