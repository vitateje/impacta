mate=25**20
mate1=(25**5)**4
print('ok %7.2f' %mate,mate1)
from math import sqrt
tec=sqrt(20)
print(tec)

raio = float(input('digite o raio: '))
n=float(3.14159)
area=(raio*raio)

a5=float(area*n)
print('o raio é igual a= %3.f'%a5)


print('AULA LINGUAGEM DE PROGRAMAÇÃO')

# Entrada
a1 = int(input('Digite um numero '))
a2 = int(input('Digite outro numero '))

# Processamento
soma = (a1 + a2)
subtrai = (a1 - a2)
divisao = (a1 // a2)
multiplica = (a1 * a2)

# Saida
print('a soma desses dois numeros é: ', soma, 'voce concorda?')
print('a subtração desses dois numeros é: ', subtrai, 'voce concorda?')
print('a soma divisao desses dois numeros é: ', divisao, 'voce concorda?')
print('a soma multiplicação desses dois numeros é: ', multiplica, 'voce concorda?')

#
a1 = int(input('Digite sua idade '))
a2 = int(input('Digite a idade da sua mae '))
a3 = (a1 + a2)
print('a soma das idades é: ', a3, 'voce concorda?')

numero = int(input('digite um numero para saber o dobro, o triplo e o quadrado de um numero: '))

print(numero * 2)
print(numero * 3)
print(numero * numero)

##
n1 = float(input('Digite a nota da AC1: '))
n2 = float(input('Digite a nota da AC2: '))
n3 = float(input('Digite a nota da AC3: '))
n4 = float(input('Digite a nota da AC4: '))

totalnotas = (n1 + n2 + n3 + n4)
media = totalnotas / 7

## duas casas - % fazendo a interpolação

print('essa é a sua media: %.3f' % media)

###

metros = float(input('digite a medida dos metros para convertermos em milimetros: '))

conversao = metros * 1000

print('o valor convertido é: %.2f' % conversao)
