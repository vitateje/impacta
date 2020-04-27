#OTHERS

def IMC ():
    ALT=float(input('Altura: '))
    PESO=float(input('Peso: '))
    while ALT<0:
        ALT=float(input('Altura: '))
    while PESO<0:
        PESO=float(input('Peso: '))
    return (ALT+PESO)/2
X=IMC()
print(X)

def conta(L,N):
    c=0
    for x in L:
        if x==N:
           c +=1
    return c

def conta2(L,N):
    c=0
    for x in range(len(L)):
        if x==N:
           c +=1
    return c

L=[3,5,7,3]
x=conta(L,3)
print(x)

tup=(1,2,3,4)
print(tup)

teste=[1,2,3,4,5]
print(teste)
print(teste[1])

#LISTAS
lista=[10,20,30,40]
tupla=(10,20,30,40)

lista[2]=777

tupla[2]
print(tupla[2]) #Indexão - Índice

print(type (tupla))
print(type (lista))

#FUNÇÃO - SEMPRE QUE HOUVER PARAMETRO NAO USAR O INPUT NA FUNÇÃO

#EX 5

def ind_maior_item(lista):
    maior=0
    #m=lista[0] # ERRADO PRA CARAMBA
    for i in range(1, len(lista)): #len tamanho de indices de uma lista
       if lista[i] > lista[maior]:
           maior=i
    return maior

def maior_item(lista):
    maior=lista[0]
    for i in range(1, len(lista)): #len tamanho de indices de uma lista
       if lista[i] > maior:
           maior=lista[i]
    return maior

#BUSCA

lista2=[80,90,10,100,50]
80 in lista2

def busca(x,s):
    for i in range(len(s)):
        if s[i]==x:
            return True
    return False

lista3=[1,2,3,4]
busca(1,lista3)
