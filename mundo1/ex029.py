
velo=int(input('digite a velocidade do carro: '))

if velo>80:
    multa = (velo - 80) * 7
    print(f'Voce Ultrapassou o limite de velocidade e vai ser multado em {multa} reais')
else:
    print('Voce esta dentro do limite de velocidade')


