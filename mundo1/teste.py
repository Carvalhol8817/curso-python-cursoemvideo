
print("Calculadora Simples")
print("--"*20)
num1=int(input("Digite um numero: "))
num2=int(input("Digite outro numero: "))
op=str(input("Digite o operador: "))
print("--"*20)
if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("Erro na operacao!")
print("--"*20)




