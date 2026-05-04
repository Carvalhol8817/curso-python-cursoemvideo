# ler comprimento de tres retas
n1=float(input('digite o primeiro comprimento:'))
n2=float(input('digite o segundo comprimento:'))
n3=float(input('digite o terceiro comprimento:'))

if n1<n2+n3 and n3<n1+n3 and n3<n2+n1:
    print('Esses comprimentos podem formar um triangulo')
else:
    print('Esses comprimentos nao podem formar um triangulo')