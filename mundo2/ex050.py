print(f'{'-='*11:^4}')
print('Somando numeros pares!')
print(f'{'-='*11:^4}')

s=0

for i in range(1,7):
    n=int(input("digite um numero: "))
    if n%2==0:
        s+= n

print(f'{'-='*18:^4}')
print(f'O valor total da soma dos pares e {s}')
print(f'{'-='*18:^4}')