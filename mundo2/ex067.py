cont=multiplicar=0

n = int(input('Digite o número que deseja saber a tabuada: '))

while True:
    cont=0
    while True:
        cont+=1
        multiplicar=n*cont
        print(f'{f'{n} x {cont} = {multiplicar}':^30}')
        if cont==10:
            break

    print('-'*40)
    print(f'Essa é a tabuada de {n}!')
    print('-'*40)
    n = int(input('Digite o número que deseja saber a tabuada: '))
    if n <= 0:
        break
print('=-='*20)
print(f'{' FIM ':-^60}')
print('=-='*20)
