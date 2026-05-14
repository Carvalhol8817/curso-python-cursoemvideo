#programa le nome idade e sexo de 4 pessoas
print('-='*10)
print('Leitura de dados')
print('-='*10)

soma=0
mu=0
maior=0
nvelho=0

for l in range(1,5):
    n=str(input('Digite seu nome: '))
    i=int(input('Digite sua idade: '))
    s=str(input('Digite seu sexo H/M: ')).upper().replace(' ','')
    print('-=' * 10)
    soma+=i

    if l==1:
        maior=i
        nvelho=n
        menor=i
        nnovo=n

    else:
        if i>maior and s=='H':
            maior=i
            nvelho=n

        if i<20 and s=='M':
            mu+=1

print(f'A média de idade do grupo é de {soma/4} anos.')
print(f'O nome do homem mais velho é de {nvelho.capitalize()}.')
print(f'Nesta Lista tem {mu} mulher/ mulheres com menos de 20 anos.')
# no final mostra a media de idade do grupo
#qual o nome do homem mais velho
#quantas mulheres tem menos de 20 anos