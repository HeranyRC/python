from random import randint as r

rTupla=(r(1,10),r(1,10),r(1,10),r(1,10),r(1,10))
media=0

for c in rTupla:
    media+=c
media/=len(rTupla)

print(f'Os numeros gerados foram {rTupla}')
print(f'O maior numero é o {max(rTupla)}')
print(f'O menor numero é o {min(rTupla)}')
print(f'A media entre os numeros é {media}')