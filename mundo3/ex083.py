# Programa onde o usuário digita uma expressão qualquer que use parênteses.
# O programa deve analisar:
# Se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expr=str(input('Digite a expressao:'))
pilha=[]
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        pilha.append(')')
if len(pilha)%2==0:
    print('Sua expressão está correta.')
else:
    print('Sua expressão está incorreta.')