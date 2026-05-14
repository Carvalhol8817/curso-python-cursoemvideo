verde = '\033[1;32m'
vermelho = '\033[1;31m'
amarelo = '\033[1;33m'
branco = '\033[1;40m'
limpo = '\033[m'

print(f'{' Lojas Carvalho ':=^40}')
preco= float(input('Digite o valor normal do produto: '))
pag=input('Formas de pagamento:\n'
          '[1] A vista dinheiro ou cheque\n'
          '[2] A vista cartao\n'
          '[3] Parcelado em ate 2x no cartao\n'
          '[4] Parcelado em 3x ou mais no cartao\n'
          'Digite o numero da opcao correspondente: ')

# A vista dinheiro/cheque = 10% de desconto
if pag == '1':
    print(f'{verde}O maximo de desconto que podemos dar e de 10%.\n'
          f'E o preco final do produto e de {preco-(preco*0.10)}{limpo}')

#a vista no cartao = 5% de desconto
elif pag=="2":
    print(f'{amarelo}A vista no cartao o maximo de desconto que conseguimos dar e de 5%{limpo}\n'
          f'{amarelo}e o valor final do produto e de {preco-(preco*0.05)}{limpo}')

# em ate 2x no cartao = preco normal
elif pag=='3':
    print(f'{vermelho}Infelizmente nao conseguimos dar desconto para essa forma de pagamento{limpo}\n'
          f'{vermelho}O valor final do produto e de {preco} reais.{limpo}')

#3x ou mais no cartao = 20% de juros
elif pag=='4':
    print(f'{branco}Como o parcelamento e em mais de duas vezes, cobramos juros de 20%.{limpo}\n'
          f'{branco}O valor final do produto e de {preco + (preco*0.20)} reais, com os juros incluidos.{limpo}')

else:
    print(f'{vermelho}Opcao Digitada nao existe!{limpo}')