nota1=float(input('Qual a primeira nota do aluno: '))
nota2=float(input('Qual a segunda nota do aluno: '))
media=(nota1+nota2)/2

if media < 5:
    print(f'A Media e de {media}.\n'
          f' {'\033[1;31m'}Aluno REPROVADO{'\033[m'}')

#Media entre 5.0 a 6.9: Recuperacao
elif media < 7:
    print(f'A Media e de {media}.\n'
          f' {'\033[1;33m'}Aluno em RECUPERACAO{'\033[m'}')

#Media 7.0 ou superior: Aprovado
elif media >=7:
    print(f'A Media e de {media}.\n'
          f'{'\033[1;32m'}Aluno APROVADO{'\033[m'}')
if media == 10:
    print(f'{'\033[1;32m'}NOTA MAXIMA \n'
          f'ALUNO EXEMPLAR{'\033[m'} ')