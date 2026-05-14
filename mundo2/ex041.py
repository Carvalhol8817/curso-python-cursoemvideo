from datetime import date

print(f'{'\033[1;36m'}-={'\033[m'}'* 20)
print(f'{'\033[1;36m'}A confederacao nacional de Natacao{'\033[m'}')
print(f'{'\033[1;36m'}-={'\033[m'}'* 20)

ano=int(input('Qual o ano de nascimento do atleta? '))
idade=date.today().year-ano

#ate 9 anos: MIRIM
if idade<=9:
    print(f' O atleta tem {idade} anos, sendo assim esta na categoria MIRIM. ')

#ate 14 anos: INFANTIL
elif idade>9 and idade<=14:
    print(f'O atleta tem {idade} anos, sendo assim esta na categoria INFANTIL.')

#ate 19 anos: JUNIOR
elif idade>14 and idade<=19:
    print(f'O atleta tem {idade} anos, sendo assim esta na categoria JUNIOR.')

#ate 20 anos: SENIOR
elif idade == 20:
    print(f'O atleta tem {idade} anos, sendo assim esta na categoria SENIOR.')

#acima: MASTER
elif idade>20 and idade<70:
    print(f'O atleta tem {idade} anos, sendo assim esta na categoria MASTER.')

elif idade>=70:
    print(f'O atleta tem {idade} anos, sendo assim ta na hora de para de nadar ja!!')
