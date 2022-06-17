numeros=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezaseis','dezasete','dezoito','dezanove','vinte')
flag=True

while flag:
    num=int(input('Digite um numero no intervalo de 0 a 20: '))
    if num<0 or num>=21:
        flag=True
        print('Numero invalido, tente novamente!')
    else:
        flag=False
print(f'Voce Digitou {numeros[num]} !')