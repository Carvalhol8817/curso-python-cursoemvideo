from time import sleep
n1 = int(input('Digite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))
print('-' * 30)
sleep(0.5)
op=0

while not op==5:

    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair')
    op=int(input('Digite a operção que quer realizar: '))
    print('-' * 30)


    if op==1:
        soma = n1+n2
        print(f'A soma entre {n1} e {n2} é {soma}')
        print('-' * 30)
    elif op==2:
        multiplicar = n1*n2
        print(f'A multiplicação de {n1} e {n2} é de {multiplicar}')
        print('-' * 30)
    elif op==3:
        maior = 0
        if n1>n2:
            maior = n1
            print(f'O primeiro valor é o maior')
            print('-' * 30)
        if n1<n2:
            maior = n2
            print(f'O segundo valor é o maior')
            print('-' * 30)
    elif op==4:
        n1 = int(input('Digite o primeiro valor inteiro: '))
        n2 = int(input('Digite o segundo valor inteiro: '))
        print('-' * 30)
        sleep(1)
    elif op==5:
        print('Finalizando...')
        sleep(2)
    else:
        print('Opcao invalida. Tente novamente.')
    print('=-='*10)

print('Fim do programa! Volte sempre!')

