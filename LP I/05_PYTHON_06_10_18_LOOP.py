''' AULA 06 - LOOP'''

#CONTADOR

qtd=0
n=float(input('Digite um numero real: '))
while n!=-1:
    qtd=qtd+1
    n=float(input('Digite um numero real: '))
print('Quantidade: ',qtd)

#ACUMULADOR

soma=0
n=float(input('Digite um numero real: '))
while n!=-1:
    soma=soma+n
    n=float(input('Digite um numero real: '))
print('Soma: %.2f' % soma)

#SOMA #MEDIA

qtd=0
soma=0
n=float(input('Digite um numero real: '))
while n!=-1:
    soma=soma+n
    qtd=qtd+1
    n=float(input('Digite um numero real: '))
media=soma/qtd
print('Media: %.2f' % media)

#MENOR E MAIOR

n=int(input('Valor: '))
menor=n
while n != -1:
    if n < menor:
        menor=n
    n = int(input('Valor: '))
print('Menor:' , menor)

#REPETIÇÃO DO PROGRAMA COM WHILE TRUE + BREAK

while True:
    n = int(input('Valor: '))
    menor = n
    while n != -1:
        if n < menor:
            menor = n
        n = int(input('Valor: '))
    print('Menor:', menor)
    repetir = input('Deseja Repetir? ')
    if repetir != 'sim': break  # interrompe o laço
