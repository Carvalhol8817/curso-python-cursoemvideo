import math
n1=float(input("qual o cateto oposto? "))
n2=float(input("qual o cateto adjacente? "))
n3=math.sqrt(math.pow(n1,2)+math.pow(n2,2))
print(f"Se o Cateto oposto tem o valor de {n1} e o cateto adjacente tem o valor de {n2}"
      f" entao o valor da hipotenusa e {n3:.2f} ")
