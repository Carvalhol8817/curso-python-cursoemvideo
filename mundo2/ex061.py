print('-' * 30)
print('Descobrindo a Progressao Aritmética')
print('-' * 30)

pt=int(input('Primeiro termo: '))
r=int(input('Razão: '))

cont=1

while cont<=10:
    pa=pt+(cont-1)*r
    cont+=1
    print(f'{pa} -> ', end='')

print('ACABOU')