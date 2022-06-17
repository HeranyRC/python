expressao=input('Digite uma expressao com parentesis: ')
pilha=[]

for s in expressao:
    if s=='(':
       pilha.append('(') 
    elif s==')':
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha)==0:
    print('A sua expressao é valida')
else:
    print('A sua expressao está errada')