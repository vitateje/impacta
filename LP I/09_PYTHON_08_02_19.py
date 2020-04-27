def Ehprimo(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

def ListaPrimos(n):
    lista = []
    for i in range(2,n):
        if Ehprimo(i):
            lista.append(i)
    return lista

print(ListaPrimos(int(input('Informe um numero: '))))

#faça uma função que receba um numero e faça a decomposição desse numero e crie uma lista com os numeros primos.

def Decomposicao(n):
    lista=[]
    while ListaPrimos

def decomporEmPrimo(x)
    primo = 2
    listaPrimos = []
    pot=0
    while (x/primo !=1):
        x=x/primo
        pot+=1
        if (x%primo !=0):
            if (pot > 0) :
                listaPrimos + [primo , pot]
                primo = proxPrimo(primo)
                pot = 0
        if (x == 1):
            return listaPrimos