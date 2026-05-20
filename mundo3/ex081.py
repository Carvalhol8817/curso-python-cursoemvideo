# Programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# c) Se o valor 5 foi digitado e está ou não na lista.

num=[]

while True:
    num.append(int(input('Digite um valor: ')))

    while True:
        resp=input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break

    if resp == 'N':
        print()
        break

print(f'{len(num)} numeros foram digitados')
print()
num.sort(reverse=True)
print(f'Lista em ordem decrescente: {num}')
print()
if 5 in num:
     print(f'O valor 5 foi digitado e esta na lista')
else:
     print('O numero 5 nao esta na lista')
