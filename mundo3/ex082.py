# Programa lê vários números e colocar em uma lista.
# Depois disso, crio duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados.
# Ao final, mostra o conteúdo das três listas geradas.
num=[]
pares=[]
impares=[]
while True:
    num.append(int(input('Digite um valor: ')))
    while True:
        resp=input('Deseja continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'N':
        print()
        break

for item in num:
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print('-='*30)
print(f'Os valores digitados foram: {num}')
print(f'Os valores pares foram: {pares}')
print(f'Os valores impares foram: {impares}')