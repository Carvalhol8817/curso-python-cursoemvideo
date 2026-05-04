#pergunte o salario de um funcionario
sal=float(input('qual o seu salario:'))

#calcule seu aumento acima de 1.250 10% abaixo 15%
if sal > 1250:
    sal2 = sal * 0.10 + sal
    print(f'Seu salario com Aumento e {sal2}')
else:
    sal2 = sal * 0.15 + sal
    print(f'Seu salario com Aumento e {sal2}')
