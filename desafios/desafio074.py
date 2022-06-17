from random import randint as r

rTupla=(r(1,10),r(1,10),r(1,10),r(1,10),r(1,10))
maior=0
menor=99
media=0

for c in rTupla:
    media+=c
    if maior<c:
        maior=c
    if menor>c:
        menor=c
media/=len(rTupla)
print(f'Os numeros gerados foram {rTupla}')
print(f'O maior numero é o {maior}')
print(f'O menor numero é o {menor}')
print(f'A media entre os numeros é {media}')