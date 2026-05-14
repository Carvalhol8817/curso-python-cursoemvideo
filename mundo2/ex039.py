from datetime import date

ano=int(input('Digite seu ano de nascimento: '))

idade=date.today().year - ano

# se ele ainda vai se alistar ao servico militar,
if idade<18:
    print(f'Voce faz {idade} anos em {date.today().year}, e nao chegou o momento de se alistar.\n'
          f'Falta {18-idade} ano/anos para se alistar.\n'
          f'Voce tem que se alistar em {date.today().year + (18-idade)}.')

# se e a hora de se alistar
elif idade==18:
    print(f'Voce faz {idade} anos em {date.today().year}, voce tem que se alistar esse ano sem falta.')

# se ja passou do tempo do alistamento
else idade>18:
    print(f'Voce faz {idade} anos em {date.today().year}, e esta em {'\033[1;31m'}Debito com o Servico Militar Brasileiro.{'\033[m'}\n'
          f'Voce esta {idade-18} ano/anos atrasado para se alistar.\n'
          f'Deveria ter se alistado em {date.today().year - (idade-18)}.\n'
          f'Compareca a junta militar mais proxima e leve seus documentos para regularizacao.')
