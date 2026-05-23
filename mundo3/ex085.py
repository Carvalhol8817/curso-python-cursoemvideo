# Programa onde o usuario digita 7 valores e sao cadastrados em uma lista unica que separa os valores pares e impares
# No final mostra os valores pares e impares em ordem crescentes

grupo=[[],[]]

for c in range (1,8):
    valor=int(input(f'Digite o {c} valor: '))

    if valor % 2 == 0:
        grupo[0].append(valor)
    else:
        grupo[1].append(valor)

grupo[0].sort()
grupo[1].sort()

print(grupo)
print(f'Os valores pares digitados foram: {grupo[0]}')
print(f'Os valores ímpares digitados foram: {grupo[1]}')