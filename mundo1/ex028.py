from random import randint
from time import sleep

print('-=-'*25)
print('Vou pensar em um numero entre 0 e 5. Voce consegue advinhar qual e?')
print('-=-'*25)

n1= randint(0,5) #Computador sorteia o numero
n2 = int(input('Em que numero eu pensei? ')) #Usuario coloca um numero
print('PROCESSANDO...')
sleep(2)

if n1 == n2: #Se n1 igual a n2
    print('Voce acertou, Parabens Voce e Fera!') #Bloco True
else:
    print(f'Voce errou,{n1} foi o que eu pensei, tente novamente!') #Bloco False