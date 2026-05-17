soma=cont=c=menor=0
nome=''
while True:
    n=str(input('Digite o nome do produto: ')).strip().capitalize()
    p=float(input('Digite o valor do produto: R$'))
    soma+=p
    c+=1

    if p>=1000:
        cont+=1

    if c==1 or p<menor:
        menor=p
        nome=n

    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N' or p == 0:
        break

print(f'O total da compra foi R${soma:.2f}')
print(f'{cont} produtos custam mais de R$1000')
print(f'O nome do produto mais barato é {nome} que custa R${menor:.2f}')
