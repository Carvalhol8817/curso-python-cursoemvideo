from _pyrepl.commands import end

print('-='*15)
print('Descobrindo numero primo')
print('-='*15)

n=int(input("digite um numero: "))
s=0

for i in range(1, n + 1):
    if n%i==0:
        print('\033[1;32m',i,end='')
        s=s+1
    else:
        print('\033[1;31m',i,end='')
if s==2:
    print('\n\033[mÉ um numero primo')
else:
    print('\n\033[mNão é um numero primo')

