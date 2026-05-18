# Programa feito com Tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro.
#  Depois mostrando:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

brasileirao=('Palmeiras','Flamego','Fluminense','São Paulo','Atlético-PR','Bragantino','Coritiba',
             'Bahia','Botafogo','Atlético Mineiro','Internacional','Vasco','Cruzeiro','Vitória','Grêmio',
             'Santos','Corinthians','Remo','Mirassol','Chapecoense')
verde='\033[1;32m'
vermelho='\033[1;31m'
limpo='\033[m'


cont=0
print('='*30)
print('Os primeiros 5 colocados:')
print('='*30)
for times in brasileirao[:5]:
    cont+=1
    print(f'{verde}Em {cont} lugar esta o {times}{limpo}')
print('='*30)

cont=17
print('Os últimos 4 colocados:')
print('='*30)
for times in brasileirao[-4:]:
    print(f'{vermelho}Em {cont} lugar esta o {times}{limpo}')
    cont += 1
print('='*30)

print('Os Times em Ordem Alfabética:')
print('='*30)
r=sorted(brasileirao)
for times in r:
    print(times,', ', end=' ')
print()
print('='*30)

print(f'{vermelho}Chapecoense está na posição {brasileirao.index('Chapecoense')+1} do brasileirão.{limpo}')
