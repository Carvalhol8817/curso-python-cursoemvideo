# Programa onde o usuário digita vários valores numéricos e cadastra numa lista.
# Nao aceita numeros duplicados
# No final são exibidos todos os valores únicos digitados, em ordem crescente

num=[]
while True:
    valor=input('digite um numero: ')
    try:
        valor=int(valor)

        if valor in num:
            print('numero duplicado, nao adicionado')
        else:
            num.append(valor)
            print('numero adicionado com sucesso')

        if all(isinstance(item,int) for item in num):
            print()
    except ValueError:
        print('Voce nao digitou um numero.')
        resp=str(input('Deseja continuar? [S/N] ')).strip().upper()

        if resp == 'N':
            break
num.sort()
print(num)