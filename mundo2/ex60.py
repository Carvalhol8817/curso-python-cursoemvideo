print('-' * 30)
print('Descobrindo Fatorial')
print('-' * 30)

n=int(input('digite um numero: '))
print('\n')

soma=1
c=n
print(f'{c}! = ', end='')

while c>0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    soma=soma*c
    c-=1


print(f'{soma}')
print('\n')
print(f'O fatorial de {n} é {soma}!')

