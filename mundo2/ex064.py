cont=soma=0
n=int(input('Digite um número [999 para parar]: '))

while n!=999:
    soma+=n
    cont += 1
    n=int(input('Digite um número [999 para parar]: '))
print(f'{cont} números foram digitados, e a soma deles é de {soma}')
print('FIM')