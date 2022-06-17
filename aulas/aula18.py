dados=[]
dados.append('Roger')
dados.append(22)
pessoas=[]
pessoas.append(dados[:])
dados[0]='Herany'
dados[1]='23'
pessoas.append(dados[:])

print(dados)
print(pessoas)
