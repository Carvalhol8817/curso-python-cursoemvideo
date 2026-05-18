# Programa têm uma tupla com várias palavras (sem acento).
# Mostra em cada palavra, quais são as respectivas vogais.

p=('aprender','programar','linguagem','python',
   'curso','grupo','gratis','estudar','mercado',
   'praticar','trabalhar','mercado','programador','futuro')

for c in p:
    print(f'\nNa palavra {c.upper()} temos ',end='')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')
