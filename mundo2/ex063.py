print('-' * 35)
print('Sequencia de Fibonacci')
print('-' * 35)

n=int(input('Quantos termos quer ver: '))
a=0
b=1
cont=0

while cont!=n:
    print(a, end=' -> ')

    proximo=a+b
    a=b
    b=proximo

    cont+=1

print('FIM')
