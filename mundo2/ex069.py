cont=maior=homen=mulher=0

while True:
    cont += 1
    print('-' * 22)
    print(f'CADASTRO DE PESSOAS {cont}')
    print('-' * 22)
    i=int(input('Qual sua idade? '))
    s=' '
    while s not in 'HM':
        s=str(input('Qual sua sexo? [H/M] ')).strip().upper()[0]
    print('-'*22)

    if i>=18:
        maior+=1

    if s=='H':
        homen+=1

    elif s=='M' and i<20:
        mulher +=1
    c=' '
    while c not in 'SN':
        c=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if c in 'Nn':
        break

print(f'{maior} pessoas são maiores de idade.')
print(f'{homen} Homens foram cadastrados.')
print(f'{mulher} mulheres têm menos de 20 anos.')
