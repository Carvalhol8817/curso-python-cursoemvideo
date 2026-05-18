# Programa com uma tupla única com nomes de produtos e seus respectivos preços, em sequência.
# Mostra uma listagem de preços, organizando os dados em forma tabular.

t=('pao',3.00,'queijo',3.00,'requeijo',5.00,'mortadela',4.00,'leite',5.50)

print('-'*43)
print(f'{'LISTAGEM DE PREÇOS':^43}')
print('-'*43)
for item in range(0,len(t)):
    if item % 2 == 0:
        print(f'{t[item]:.<30}',end=' ')
    else:
        print(f'R${t[item]:>10.2f}')
print('-'*43)
