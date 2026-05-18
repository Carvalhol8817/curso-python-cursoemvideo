# Programa lê número e o digita por extenso
# Usando variavéis compostas (tuplas)
while True:
     num=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove',
          'dez','onze','doze','treze','quatorze','quinze','dezesseis',
          'dezessete','dezoito','dezenove','vinte')
     while True:
          r=int(input('Digite um numero entre 0 e 20: '))
          if 0<=r<=20:
               break
          print('\nTente novamente. ',end='')

     print('Você digitou o número',num[r])
     print()
     while True:
          c=str(input('Quer escolher outro número? [S/N]')).strip().upper()[0]
          if c in 'SN':
              break
          else:
               print('\nDigite apenas S ou N. ',end='')
     if c in 'Nn':
          break
