import random
from time import sleep


branco = '\033[1;40m'
vermelho = '\033[1;31m'
verde = '\033[1;32m'
amarelo = '\033[1;33m'
ciano='\033[1;36m'
limpo='\033[m'

def limpar():
  print('\n'*50)


pts_usuario= 0
pts_comp=0
r='S'

while r!='N':

      print(f'{branco}{'-'*20:^40}{limpo}')

      print(f'{branco}{'VAMOS JOGAR JOKENPO?':^40}{limpo}')

      print(f'{branco}{'-'*20:^40}{limpo}')
      sleep(0.5)

      print(f'{branco}{'pedra':^40}{limpo}\n'
            f'{branco}{'':^40}{limpo}\n'
            f'{branco}{'papel':^40}{limpo}\n'
            f'{branco}{'':^40}{limpo}\n'
            f'{branco}{'tesoura':^40}{limpo}')

      sleep(0.5)
      print(f'{branco}{'':^40}{limpo}')

      usuario= input(f'{branco}{'Digite sua escolha:':^40}{limpo}').strip().lower()
      sleep(0.5)

      lista=['pedra','papel','tesoura']
      comp=random.choice(lista)

      print('JO')
      sleep(1)
      print('KEN')
      sleep(1)
      print('PO!!!')

      print('-='*15)
      print(f'Computador jogou {comp}\n'
            f'Jogador jogou {usuario}')
      print('-=' * 15)

      #VITORIAS DO USUARIO#
      if usuario=='pedra' and comp=='tesoura':
            print(f'{verde}Voce Ganhou, A {usuario} esmagou a {comp} do computador.{limpo}')
            pts_usuario+=1

      elif usuario=='papel' and comp=='pedra':
            print(f'{verde}Voce Ganhou, O {usuario} embalou a {comp} do computador.{limpo}')
            pts_usuario+=1

      elif usuario=='tesoura' and comp=='papel':
            print(f'{verde}Voce Ganhou, A {usuario} cortou o {comp} do computador.{limpo}')
            pts_usuario += 1

      #VITORIAS DO COMPUTADOR#
      elif comp == 'pedra' and usuario == 'tesoura':
            print(f'{vermelho}Voce perdeu, A {comp} quebrou a sua {usuario}.{limpo}')
            pts_comp+=1

      elif comp == 'papel' and usuario == 'pedra':
            print(f'{vermelho}Voce perdeu, O {comp} embalou a sua {usuario}.{limpo}')
            pts_comp += 1

      elif comp == 'tesoura' and usuario == 'papel':
            print(f'{vermelho}Voce perdeu, A {comp} cortou o seu {usuario}.{limpo}')
            pts_comp += 1

      #EMPATES#
      elif usuario == comp:
            print(f'{amarelo}EMPATOU, Voce e computador jogaram {usuario}.{limpo}')

      else:
            print('Escolha Invalida!')

      print('Placar:\n'
            f'usuario: {pts_usuario}\n'
            f'computador: {pts_comp}\n')

      r=str(input('Quer jogar novamente? S/N: ')).strip().upper()
      limpar()



