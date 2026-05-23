# Programa cria uma matriz de dimensao 3x3 e preenche com valores lidos pelo teclado
# no final mostra a matriz na tela com a formatacao correta

matriz = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        valor = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        matriz[linha].append(valor)

print('-=' * 20)

for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()