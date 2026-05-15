from random import randint
from time import sleep

vermelho = '\033[0;31m'
verde = '\033[0;32m'
limpo = '\033[m'

print('-='*10)
print('Jogo da Advinhação')
print('-='*10)

print('Vou pensar em um numero entre 1 e 10\n')
print('Pensando...\n')
sleep(1)

computador = randint(1, 10)
print('Pronto, já escolhi meu número!')
sleep(1)

usuario=0
palpites=0

while computador!=usuario:
    usuario = int(input('Qual numero entre 1 e 10 eu escolhi? \n'))
    palpites += 1
    if usuario!=computador:
        if usuario<computador:
            print (f'{vermelho}Mais... tente mais uma vez.{limpo}\n')
        else:
            print(f'{vermelho}Menos... tente mais uma vez.{limpo}\n')
    else:
        print(f'{verde}Acertou, eu pensei no número {computador}.\n'
              f'E você precisou de {palpites} tentativas para acertar.{limpo}')
