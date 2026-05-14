from datetime import date

maior=0
menor=0

for i in range (1,8):
    ano = int(input(f'{i}-Digite o ano de nascimento: '))
    if date.today().year - ano >= 18:
        maior +=1
    else:
        menor += 1

print(f'{maior} pessoas já são maiores de 18 anos')
print(f'{menor} pessoas são menores de 18 anos')
