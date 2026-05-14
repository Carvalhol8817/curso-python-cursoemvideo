#Escreva um programa que leia 2 numeros inteiros e compare-os
# mostre na tela a mensagem 'O primeiro valor e maior ' 'o segundo valor e maior ' ' nao existe valore maior, os dois sao iguais'
n1=int(input('Digite o primeiro numero inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))

if n1>n2:
    print(f'O PRIMEIRO valor {n1} e maior ')

elif n2>n1:
    print(f'O SEGUNDO valor {n2} e maior')

else:
    print('Os dois valores sao IGUAIS')
