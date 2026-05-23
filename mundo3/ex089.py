# Programa que leia nome e duas notas de varios alunos, guarda tudo numa lista composta
# Mostra um boletim contendo a media de cada um
# Permita que o usuario possa mostrar as notas de cada aluno individualmente
temp=[]
grupo=[]

while True:
    nome=str(input('Nome: ')).strip().capitalize()
    nota1=float(input('Nota 1: '))
    nota2=float(input('Nota 2: '))
    media=(nota1+nota2)/2
    temp.append(nome)
    temp.append(nota1)
    temp.append(nota2)
    temp.append(media)
    grupo.append(temp[:])
    temp.clear()

    while True:
        resp=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp in 'N':
        break

while True:
    print('-=' * 26)
    print(F'{'BOLETIM':^52}')
    print('-=' * 26)
    print()
    for i in range(len(grupo)):
        print(f'Aluno {i}: {grupo[i][0]:.<30} Média: {grupo[i][3]}')

        print()
    while True:
        print('-='*26)
        r=int(input('Qual numero do aluno que deseja ver as notas? '))
        print('-='*26)
        if 0<=r<len(grupo):
            break
        else:
            print('Número invalido, tente novamente...')
            print()
    print()
    print(f'Aluno {r}: {grupo[r][0]:.<30} ', end='')
    print(f'Nota 1: {grupo[r][1]}', end='')
    print(f' /Nota 2: {grupo[r][2]}')
    print()
    print('-='*33)
    print()
    while True:
        r2=str(input('Quer ver a nota de outro aluno? [S/N] ')).strip().upper()[0]
        if r2 in 'SN':
            break
    if r2 in 'N':
        break
