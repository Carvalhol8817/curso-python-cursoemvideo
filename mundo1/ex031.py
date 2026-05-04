viagem= int(input('Qual a distancia da viagem:'))

if viagem<=200:
    valor1 = viagem*0.50
    print(f'O valor da passagem vai ficar {valor1} reais')
else:
    valor1 = viagem*0.45
    print(f'O valor da passagem vai ficar {valor1} reais')
