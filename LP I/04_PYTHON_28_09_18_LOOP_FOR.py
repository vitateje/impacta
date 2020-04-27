# CORREÇÃO AC4

#n=int(input('Valor?'))
#while n<20 or n >30:
#  n=int(input('Valor?'))
#print('boa noite')

maior_idade=input('voce é maior de idade?')
while maior_idade == 'não':
    print('Nada de video games violentos')
    maior_idade=input('Voce é maior de idade:')
print('Voce é maior de idade:')

# Dados numero naturais (um por vez) conte quantos valores foram
# foram inseridos pelo usuario ate que seja inserido um impar (que nao devera ser contabilizado).


n=int(input('Valor: '))
cont=0
while n%2 ==0:
    cont=cont+1
    n=int(input('Valor: '))
print('Pares:', cont)

#FOR - iniciar com variavel controladora

#[0,5[
for cont in range(5):
    print('boa noite')

cont=0
while cont<5:
    print('Boa Noite')
    cont=cont+1

#[0,n[    
n=int(input('Quantas Repetições'))
for cont in range(n):
    print(cont)

#[2,n[
ini=int(input('começa com qual valor?'))
fim=int(input('Pára em qual valor?'))
for cont in range(ini,fim):
    print(cont)

#[2,n,passo[
ini=int(input('começa com qual valor?'))
fim=int(input('Pára em qual valor?'))
for cont in range(ini,fim,2):
    print(cont)   
