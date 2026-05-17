saque=int(input('Qual o valor do saque: '))

c=v=d=um=0

while True:
    while not saque < 50:
        saque-=50
        c+=1

    while not saque < 20:
        saque-=20
        v+=1

    while not saque < 10:
        saque-=10
        d+=1

    while not saque == 0:
        saque-=1
        um+=1

    if saque == 0:
        break

print('='*30)
print(f'''Total de {c} cédulas de R$50
Total de {v} cédulas de R$20
Total de {d} cédulas de R$10
Total de {um} cédulas de R$1''')
print('='*30)
