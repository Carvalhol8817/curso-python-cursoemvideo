n1=int(input("Um valor:"))
n2=int(input("Outro valor:"))
s=n1+n2
m=n1*n2
d=n1/n2
di=n1//n2
e=n1%n2
print("="*20)
print(" A soma vale {}".format(n1+n2),end=" ")
print("A subtracao vale {}".format(n1-n2), end=" ")
print("A multiplicacao vale {}".format(n1*n2), end=" ")
print("A divisao vale {:.2f}".format(n1/n2), end=" ")
print("A divisao inteira vale {}".format(n1//n2), end=" ")
print("A resto da divisao vale {}".format(n1%n2))
print(" A soma e {} \n A multiplicacao e {} \n A divisao e {:.2f} \n A divisao inteira e {}\n O resto da divisao e {}".format(s,m,d,di,e))