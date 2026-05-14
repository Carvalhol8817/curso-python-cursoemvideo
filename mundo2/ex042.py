
n1=float(input(f'{'\033[7;40m'}digite o primeiro comprimento:'))
n2=float(input('digite o segundo comprimento:'))
n3=float(input('digite o terceiro comprimento:'))

if n1<n2+n3 and n2<n1+n3 and n3<n2+n1:
    print(f'{'\033[0;32m'}Esses comprimentos podem formar um triangulo')

    #Equilatero=todos os lados iguais
    if n1 == n2 == n3:
        print(f'E forma um triangulo equilatero.{'\033[m'}')

    #Isosceles = dois lados iguais
    elif n1==n2 or n2==n3 or n3==n1:
         print(f'E forma um triangulo isosceles.{'\033[m'}')

    #Escaleno = todos os lados diferentes
    elif n1!=n2!=n3!=n1:
        print(f'E forma um triangulo escaleno.{'\033[m'}')

else:
    print(f'{'\033[0;31m'}Esses comprimentos nao podem formar um triangulo{'\033[m'}')

