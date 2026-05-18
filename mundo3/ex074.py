# Programa gera 5 números aleatórios e coloca em uma tupla.
# Depois disso mostra a listagem de números gerados
# também indica o menor e o maior valor que estão na tupla.

from random import randint

num=(randint(1,10), randint(1,10),randint(1,10),
     randint(1,10),randint(1,10))

for n in num:
    print(n,end=' ')

print('\n')
print(f'O maior número gerado foi {max(num)}')
print(f'O menor número gerado foi {min(num)}')
