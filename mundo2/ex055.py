print('-='*10)
print('Maior e menor peso')
print('-='*10)

for i in range(1,6):
    p=(float(input(f'Digite o peso(Kg) numero {i}: ')))

    if i==1:
        maior=p
        menor=p
    else:
        if p>maior:
            maior=p
        if p<menor:
            menor=p

print('-='*10)
print(f'O maior peso foi de {maior}Kg')
print(f'O menor peso foi de {menor}Kg')
print('-='*10)