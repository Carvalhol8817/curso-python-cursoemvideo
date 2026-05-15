soma=cont=0
r=''

while r!='N':
    n=int(input('Digite um número inteiro: '))

    cont+=1
    soma+=n

    if cont==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n

    r = str(input('Quer continuar? [S/N] ')).upper()

print('\n')
print(f'Você digitou {cont} números.')
print(f'A média entre eles é de {soma/cont}.')
print(f'O maior número foi {maior} e o menor foi {menor}.')