n1=float(input("Qual altura da parede? "))
n2=float(input("Qual largura da parede? "))
area=n1*n2
tinta=area/2
print("A parede tem o total de {} metros quadrados".format(area))
print("Como cada litro de tinta pinta 2 metros quadradados, ",end="")
print("iremos precisar de {} Litros de tinta".format(tinta))