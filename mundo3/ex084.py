# Programa lê nome e peso de varias pessoas e guarda dentro de uma lista
# quantas pessoas foram cadastradas
# uma listagem com as pessoas mais pesadas
# uma listagem com as pessoas mais leves.

lista = list()
grupo = list()
maior = menor = 0

while True:
    lista.append(str(input("Digite seu nome: ")))
    lista.append(int(input('Digite seu peso:')))
    if len(grupo) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]

    grupo.append(lista[:])
    lista.clear()

    while True:
        r=str(input("Quer continuar? [S/N] ")).upper()[0]
        if r in 'SN':
            break

    if r == 'N':
        break

print('-='*30)
print(f'{len(grupo)} pessoas cadastradas')
print(f'O maior peso foi de {maior}Kg',end=' ')
for p in grupo:
    if p[1] == maior:
        print(p[0],'...',end=' ')

print()
print(f'O menor peso foi de {menor}Kg', end=' ')
for p in grupo:
    if p[1] == menor:
        print(p[0],'...',end=' ')
print()