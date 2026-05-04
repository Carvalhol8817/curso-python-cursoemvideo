#programa le 3 numeros e mostra qual o maior e qual o menor
n1= int(input('Digite o primeiro numero: '))
n2= int(input('Digite o segundo numero: '))
n3= int(input('Digite o terceiro numero: '))

# testando maior
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

#testando menor
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

print(f'{maior} e o maior valor e {menor} e o menor valor')