import os
palpites=list()
palpites2=tuple()
count=0
zero=1

while True:
    count+=1
    num=input(f'P.{count}: ')
    if num=='':
        num=0
    if num == '999':
        break
    else:
        if len(palpites)>0:
            if num==palpites[len(palpites)-1]:
                zero+=1
                palpites[len(palpites)-1]=f'0*{zero}'                
            else:
                palpites.append(num)

        else:
            palpites.append(num)
        
os.system("cls")

print(f'Palpites: {palpites}, {zero}')