nome = str(input('Digite seu nome completo: ')).strip().split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome e {}'.format(nome[0].capitalize()))
print('Seu ultimo nome e {}'.format(nome[len(nome)-1].capitalize()))