#   Dicionarios
'''
pessoa=dict()
pessoa={'nome':'Roger','idade':22}
pessoa['sexo']='M'
pessoa['nome']='Herany'
pessoa['altura']=1.76
del pessoa['altura']

for k,v in pessoa.items():
    print(f'{k}: {v}')

for v in pessoa.values():
    print(f'{v}')

print(f'Nome: {pessoa["nome"]}')
'''
# print(pessoa)
#print(pessoa.values())
#print(pessoa.keys())
#print(pessoa.items())

familia=list()
pessoas=dict()

for c in range(7):
    pessoas['nome']=input(('Nome: '))
    pessoas['idade']=int(input('Idade: '))
    familia.append(pessoas.copy())
for v in familia:
    print(f'{v}')