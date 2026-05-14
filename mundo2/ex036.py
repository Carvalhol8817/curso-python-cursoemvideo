print(f"{'\033[1;32m'}-=-{'\033[m'}" * 13)
print(f'{'\033[1;31m'} Financiamento Para Imoveis Santander{'\033[m'}')
print(f"{'\033[1;32m'}-=-{'\033[m'}" * 13)

n1=float(input('Qual o Valor do Imovel desejado? R$'))
n2=float(input('Qual o seu salario? R$'))
n3=int(input('Em quantos anos deseja pagar? '))

mensa=((n1/n3)/12)
min= (n2*0.30)

if min>=mensa:
    print(f'{'\033[7;32;40m'} Seu Financiamento Foi APROVADO {'\033[m'}')
    print(f'Para pagar um imovel de R${n1:.2f} reais em {n3} anos a prestacao sera de {mensa:.2f}')
else:
    print(f'{'\033[7;31;40m'}Infelizmente seu financiamento foi NEGADO{'\033[m'}')
    print(f'Para pagar um imovel de R${n1:.2f} reais em {n3} anos a prestacao seria de {mensa:.2f}\n'
          'Incompativel pois ultrapassa os 30% do seu salario.')

