# Programa lê 5 valores numéricos e guarda em uma lista.
# Depois mostra qual o maior e o menor valor digitado e as suas respectivas posições na lista.

lista=[]
maior=menor=0

for i in range(0,5):
    valor=int(input(f'Digite um valor para a posição {i}: '))
    lista.append(valor)
    if i==0:
        maior=menor=valor
    else:
        if valor>maior:
            maior=valor
        if valor<menor:
            menor=valor

print(f'Os numeros digitados foram: {lista}')
print('\n')
print('O MAIOR numero digitado foi ',max(lista),'e esta na/nas posicao/posicoes: ',end='')
for pos,valor in enumerate(lista):
    if valor==maior:
        print(f'{pos}...',end='')
print()
print('O MENOR numero digitado foi ',min(lista),'e esta na/nas posicao/posicoes: ',end='')
for pos,valor in enumerate(lista):
    if valor==menor:
        print(f'{pos}...',end='')
print()
