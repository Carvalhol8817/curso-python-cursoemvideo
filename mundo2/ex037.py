print(f"{'\033[1;32m'}-=-{'\033[m'}" * 19)
print(f'{'\033[1;31m'} Conversao de inteiro para Binario, Octal ou Hexadecimal {'\033[m'}')
print(f"{'\033[1;32m'}-=-{'\033[m'}" * 19)

num=int(input('Digite um Numero inteiro: '))
base=(input('1 - Binario \n'
            '2 - Octal \n'
            '3 - Hexadecimal \n'
            'Digite o numero da Conversao que quer realizar: '))

if base == '1':
    print(f'{bin(num)[2:]} e o numero binario de {num}')

elif base == '2':
    print(f'{oct(num)[2:]} e o numero octal de {num}')

elif base == '3':
    print(f'{hex(num)[2:]} e o numero hexadecimal de {num}')

else:
    print('Voce digitou algo errado!')