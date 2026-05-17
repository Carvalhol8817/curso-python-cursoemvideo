soma=cont=0

while True:
    n=int(input('Digite um número inteiro[999 para parar]: '))
    if n==999:
        break
    soma += n
    cont += 1

print(f'{cont} números foram digitados, e a soma entre eles é de {soma}.')
