print('-' * 35)
print('Descobrindo a Progressao Aritmética')
print('-' * 35)

pt=int(input('Primeiro termo: '))
r=int(input('Razão: '))

a=''
t=10
total=0
cont=1

while t!=0:
    total+=t
    while cont<=total:
        pa=pt+(cont-1)*r
        cont+=1
        print(f'{pa} -> ', end='')

    print('PAUSA.')
    t=int(input('Quantos Termos quer mostrar a mais? '))


print('ACABOU')
print('-' * 35)
