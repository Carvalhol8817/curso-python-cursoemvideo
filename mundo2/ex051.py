print('-='*22)
print('Progressao Aritmética - 10 primeiros termos')
print('-='*22)

pt = int(input('Primeiro termo: '))
r= int(input('Qual a razão? '))

for i in range(1, 11):
    a= pt + (i-1)*r
    print(f'{a} -> ', end='')

print('ACABOU')