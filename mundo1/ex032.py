from datetime import date
ano= int(input('Digite um ano: Se quiser analisar o ano que estamos digite 0: '))
if ano == 0:
    ano= date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} e um ano bissexto')
else:
    print(f'{ano} nao e bissexto')