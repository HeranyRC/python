lista=[[],[]]

for num in range(1,8):
    n=int(input(f'Digite o {num}º valor: '))
    if (n%2)==0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f'Os pares sao {lista[0]}')
print(f'Os impares sao {lista[1]}')