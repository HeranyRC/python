num=[1,5,6,7,3]
num[2]=9
num.append(0)
num.insert(0,4)
num.pop()

if 5 in num:
    num.remove(5)

num.sort(reverse=True)

print(num)
print(f'A lista tem {len(num)} elementos')
print('\n')
valores=list(range(1,11))
for v in valores:
    print(f'{v}',end=' ')
print('\n')
for c,v in enumerate(valores):
    print(f'Encontrei o valor {v} na posicao {c}')
print('Isso foi tudo que encontrei')