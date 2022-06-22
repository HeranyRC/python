import os
palpites=list()
palpites2=tuple()
count=0


while True:
    count+=1
    num=input(f'P.{count}: ')
    if num=='':
        num=0
    if num == '999':
        break
    else:
        palpites.append(num)

        #proxima vez usar um ciclo for para verificar se os numeros seguintes são iguais, e usar github branches
os.system("cls")

print(f'Palpites: {palpites}')