print("VAMOS CALCULAR A MEDIA DE SUAS NOTAS?")
print("-"*30)
n1=float(input("Digite a primeiro semestre:"))
n2=float(input("Digite a segundo semestre:"))
nota=(n1+n2)/2
print("A media de suas notas e {}".format((n1+n2)/2))
if nota>=70:
    print("Voce foi Aprovado")
else:
    print("Voce foi Reprovado")
