# ler comprimento de tres retas
n1=float(input(f'{'\033[7;40m'}digite o primeiro comprimento:'))
n2=float(input('digite o segundo comprimento:'))
n3=float(input('digite o terceiro comprimento:'))

if n1<n2+n3 and n2<n1+n3 and n3<n2+n1:
    print(f'{'\033[0;32m'}Esses comprimentos podem formar um triangulo{'\033[m'}')
else:
    print(f'{'\033[0;31m'}Esses comprimentos nao podem formar um triangulo{'\033[m'}')