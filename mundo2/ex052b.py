print('-='*15)
print('Descobrindo numeros primos')
print('-='*15)

n=int(input("digite um numero para ver os numeroso primos no intervalo: "))
for i in range(1, n + 1):
    s = 0
    for a in range(1, i + 1):
        if i%a == 0:
            s+=1
    if s == 2:
        print(i)



