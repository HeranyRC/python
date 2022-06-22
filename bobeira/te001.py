import os
palpites=list()
palpites2=list()
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

    for p in palpites: #range(len(palpites)):
        pass
        #proxima vez usar um ciclo for para verificar se os numeros seguintes são iguais, e usar github branches

cc=0
os.system("cls")
for c,p in enumerate(palpites):
    if c>0:    
        if p==palpites[c-1]:
            cc+=1
            palpites2[c-1]=(f'{p}*{cc}')
        else:
            palpites2.append(p)
    else:
        palpites2.append(p)


print(f'Palpites1: {palpites}')
print(f'Palpites2: {palpites2}')