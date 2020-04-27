'''Exercício: escreva uma função que recebe um número natural e devolve a 
decomposição em números primos para este número'''
def EhPrimo(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True

def ListaPrimos(n):
    lista = []
    for i in range(2,n):
        if EhPrimo(i):
            lista.append(i)
    return lista

def FatoresPrimos(n):
    fatores = []
    if EhPrimo(n):
        return [[n,1]] #caso simples, se for primo o resultado é apenas o próprio número
    for i in ListaPrimos(n//2+1):
        pot = 0
        while n % i == 0:
            pot += 1
            n /= i
        if pot > 0:
            fatores.append([i,pot]) #adiciona lista, não sabia que dava para fazer isso
    return fatores

print(FatoresPrimos(1003))


