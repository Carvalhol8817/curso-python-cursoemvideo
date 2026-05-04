nome=str(input("Qual seu nome completo?" ).strip())
print("O nome com todas as letras Maiusculas fica", nome.upper())
print("O seu nome com todas as letras minusculas fica", nome.lower())
print("O seu nome tem no total {} letras".format(len(nome) - nome.count(" ")))
primeiro=nome.split()[0]
print("O seu primeiro nome tem {} letras".format(len(primeiro)))
