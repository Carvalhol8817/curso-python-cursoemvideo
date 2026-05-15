s=str(input('Digite seu sexo [M/F]: ')).upper().strip()[0]

while s not in 'MF':
    print('digite novamente apenas M ou F')
    s=str(input('Digite seu sexo [M/F]: ')).upper().strip()

print(f'Sexo {s} registrado com sucesso')

