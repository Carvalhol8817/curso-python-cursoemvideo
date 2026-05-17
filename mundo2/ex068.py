from random import randint
from time import sleep

verde='\033[0;32m'
vermelho='\033[0;31m'
amarelo='\033[0;33m'
limpo='\033[m'

print('-'*40)
print('Vamos Jogar Par ou ímpar?')
print('-'*40)

cont=0

while True:
    r=' '
    while r not in 'PI':
        r=str(input('Par ou Ímpar? ')).strip().upper()[0]
    usu=int(input('Digite o número que quer jogar[0 a 10]: '))
    comp = randint(0, 10)
    soma=comp+usu
    print(f'{amarelo}o Computador jogou {comp}{limpo}')

    if r == 'P':
        if soma %2 == 0:
            print(f'{verde}\nParabéns você ganhou, {comp} + {usu} = {soma} e é PAR.{limpo}\n')
            cont+=1
        else:
            print(f'{vermelho}\nVocê perdeu,  {comp} + {usu} = {soma} é Ímpar.{limpo}\n')
            break

    elif r == 'I':
        if soma%2 == 1:
            print(f'{verde}\nParabéns você ganhou, {comp} + {usu} = {soma} é Ímpar.{limpo}\n')
            cont += 1
        else:
            print(f'{vermelho}\nVocê perdeu,  {comp} + {usu} = {soma} é PAR.{limpo}\n')
            break

    else:
        print(f'\n{r} é inválido, jogue novamente.\n')
    print('Vamos jogar novamente...')

print('-'*40)
print(f'{f'Você teve {cont} vitórias consecutivas':^40}')
print('-'*40)
sleep(1)
print(f'{'Fim do jogo':^40}')