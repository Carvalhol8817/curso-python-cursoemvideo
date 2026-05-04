frase=input('digite uma frase: ').strip().lower()
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A letra A aparece na posicao {} a primeira vez'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez na posicao {}'.format(frase.rfind('a')+1))
