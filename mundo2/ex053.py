#programa le uma frase qualquer e diga se ela e um polindromo.
print('-='*10)
print('É um políndromo?')
print('-='*10)

f=str(input('Digite uma frase: ')).lower().strip() #f recebe a frase digitada, remove os espaços e deixa em minúsculo

inverso='' # cria a variavel inverso para receber a frase invertida

for l in range(len(f)-1, -1, -1):
    inverso += f[l]

print(f'Frase = {f}')
print(f'Inverso = {inverso}')

if inverso == f:
    print('A frase e um políndromo.')
else:
    print('A frase não é um políndromo.')
#ex: APOS A SOPA / A SACADA DA CASA/ A TORRE DA DERROTA
# /O LOBO AMA BOLO/ ANOTARAM A DATA DA MARATONA