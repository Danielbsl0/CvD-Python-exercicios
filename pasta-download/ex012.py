preço = float(input('Digite o preço do produto:'))
desc = float(preço-preço*5/100)
print(f'O seu produto possui um preço ordinário de: R$\033[32m{preço}\033[m')
print(f'Porém na Black Friday ganhará um desconto de 5% ficando em: R$\033[34m{desc}\033[m.')
