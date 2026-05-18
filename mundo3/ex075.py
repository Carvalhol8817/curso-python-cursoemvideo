# Programa que lê quatro valores pelo teclado e guarda em uma tupla.
# Depois ele mostra:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3
# C) Quais foram os números pares.

num=(int(input('Digite o Primeiro Valor: ')),
     int(input('Digite o Segundo Valor: ')),
     int(input('Digite o Terceiro Valor: ')),
     int(input('Digite o Quarto Valor: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1} posição')
else:
    print(f'O valor 3 nao foi digitado.')
print(f'Os valores pares digitados foram: ',end=' ')
for n in num:
    if n%2==0:
        print(n, end=' ')




