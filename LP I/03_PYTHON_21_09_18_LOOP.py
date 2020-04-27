#LOOP

x=50
while x<=100:
    print(x)
    x=x+1

cont=0
while cont <= 10:#variavel de controle
   print('bom dia!')
   cont=cont+1#variavel de controle

#CONTAGEM REGRESSIVA - FIRE!
cont=10
while cont <= 10 and cont>=0:#variavel de controle
   print(cont)
   cont=cont-1#variavel de controle
print('Fogo!')
    
#PARES
cont=0
while cont<=100:
    print(cont)
    cont=cont+2

#PARES ATE O NUMERO INFORMADO#
cont=0
limite=int(input('DIGITE UM NUMERO'))
while cont<=limite:
    print(cont)
    cont=cont+2

#SENHA

PWDCAD=int(input('CADASTRE SUA SENHA - APENAS NUMEROS: '))
PWD=int(input('Digite sua senha: '))
while PWD!=PWDCAD:
    PWD=int(input('Senha errada! - Digite sua senha novamente: '))
print('Senha Correta! Finished This!')
