numeros=list()
flag=True

while flag:
    n=int(input('Digite um numero: '))
    if n in numeros:
        print('Numero duplicado, Tente outro.')
    else:
        numeros.append(n)
    resp=input('Quer continuar (s/n): ').lower()
    if resp=='s':
        flag=True
    else:
        flag=False
numeros.sort()
print(f'Os numeros digitados foram {numeros}.')



