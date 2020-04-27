#ESTRUTURA DE SELEÇÃO

teste=int(input('Digite um numero: '))
idade=int(input('digite sua idade: '))
sexo=(input('Digite M-Masculino ou F-Feminino: '))

if idade>=18 and idade<40:
    print('Que bom intervalo: ')
elif idade<18 and idade<0:
    print('menor de idade tb: ')
elif idade>=40 and idade<50:
    print('boa idade tb: ')
elif idade>=50 and idade<60:
    print('é de idade, bastante idade ')

if sexo == 'M' or sexo == 'm':
    print('Masculino de Idade')
else:
    print('Feminino de Idade')

#CALCULADORA

a=float(input('Primeiro valor: '))
b=float(input('Segundo valor: '))

op=input('escolha: +, -, * ou /:')
if op=='+':
        print('Resultado: ', a+b)
elif op=='-':
        print('Resultado: ', a-b)
elif op=='*':
        print('Resultado: ', a*b)
elif op=='/':
        print('Resultado: ', a/b)   

#ESTRUTURA DE SELEÇÃO OU CONDICIONAL

NOTA=float(input('Digite sua nota: '))
if NOTA>=6.0:
    print('Aprovado')
else:
    print('Reprovado')

#INDENTAÇÃO
n=float(input('Valor: '))
if n>8:
    print('Parabens')
    n=n+1
    print('Nova Nota: ',n)
else:
    print('Estude mais, você consegue!')
    n=n+0.1
    print('Nova nota, mas nao acostume:', n)
print('Boa noite!')

#OPERADORES RELACIONAS / LOGICOS

maca = int(input('digite a quantidade maças: '))

if maca <= 12:
    print('o valor é R$ %.2f' % (maca*1.3))
else:
    print('o valor é R$ %.2f' % (maca*1.0))

#IF / ELSE

dia=int(input('Qual dia? '))
if dia==1:
    print('Domingo')
else:
    if dia==2:
        print('Segunda')
    else:
        if dia==3:
            print('Terça')
        else:
            if dia==4:
                print('Quarta')
            else:
                if dia==5:
                     print('Quinta')
                else:
                    if dia==6:
                      print('Sexta')
                    else:
                        print('Sabado')

#ELIF

dia=int(input('Qual dia? '))
if dia==1 or dia==8:
    print('Domingo')
elif dia==2:
    print('Segunda')
elif dia==3:
    print('Terça')
elif dia==4:
    print('Quarta')
elif dia==5:
    print('Quinta')
elif dia==6:
    print('Sexta')
elif dia==7:
    print('Sabado')
