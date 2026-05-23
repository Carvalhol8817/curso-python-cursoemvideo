# Programa Cria palpites de jogos na MEGA-SENA
# Pergunta quantos jogos serao gerados
# Depois sorteia 6 numeros entre 1 e 60 para cada jogo
# cadastrando tudo em uma lista composta
from time import sleep
from random import randint

grupo=[]

print('-='*16)
print(f'{'Gerador de Jogos MEGA-SENA':^32}')
print('-='*16)

jogos=int(input('Quantos jogos você quer gerar? '))
print('-='*16)

for i in range(jogos):
    temp = [randint(1, 60),randint(1, 60),randint(1, 60),
            randint(1, 60),randint(1, 60),randint(1, 60)]
    grupo.append(temp[:])
    sleep(1)
    temp.clear()

for j in range(jogos):
    print(f'Jogo {j+1}: {grupo[j]}')
print('-='*16)
print(f'{'FIM':^32}')
print('-='*16)
