# Desafio Anterior Aprimorado, Mostrando:
# A soma de todos os valores pares digitados
# A soma dos valores da terceira coluna
# O maior valor da segunda linha

matriz = [[],[],[]]
soma=soma3=maior=0

for linha in range(3):
    for coluna in range(3):
        valor=int(input(f'Digite um valor para [{linha},{coluna}]: '))
        matriz[linha].append(valor)
        if valor % 2 == 0:
            soma+=valor
        if coluna == 2:
            soma3+=valor
        if linha==1 and coluna==0:
            maior=valor
        else:
            if linha==1 and valor > maior:
                maior=valor

print('-=' * 15)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]',end='')
    print()
print('-=' * 15)
print()
print(f'A soma de todos os valores pares: {soma}')
print(f'A soma da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha: {maior}')

