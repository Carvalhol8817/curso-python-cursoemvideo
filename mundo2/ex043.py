#programa le peso e altura do usuario
peso=float(input('Qual o seu peso?'))
altura=float(input('Qual a sua altura?'))

#calcula seu imc,
imc=peso/(altura**2)

#Mostra tabela de acordo com o imc
#Abaixo de 18.5: Abaixo do peso
if imc<18.5:
    print(f'Seu IMC e {imc:.2f}, esta abaixo do peso.')

#Entre 18.5 a 25: Peso ideal
elif imc>=18.5 and imc<25:
    print(f'Seu IMC e {imc:.2f}, esta no seu peso ideal.')

#25 ate 30: Sobrepeso
elif imc>25 and imc<30:
    print(f'Seu IMC e {imc:.2f}, esta com sobrepeso.')

#30 ate 40: Obesidade
elif imc>30 and imc<40:
    print(f'Seu IMC e {imc:.2f}, esta com obesidade.')

#acima de 40: Obesidade morbida
else:
    print(f'Seu IMC e {imc:.2f}, esta com obesidade morbida.')

