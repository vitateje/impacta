
'''Exercício: escreva uma função que recebe um número natural e devolve a 
decomposição em números primos para este número'''


def eh_primo(n):
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def lista_primos(n):
    lista = []
    for i in range(2, n):
        if eh_primo(i):
            lista.append(i)
    return lista


def fatores_primos(n):
    fatores = []
    if eh_primo(n):
        return [[n, 1]]  # caso simples, se for primo o resultado é apenas o próprio número
    for i in lista_primos(n//2+1):
        pot = 0
        while n % i == 0:
            pot += 1
            n /= i
        if pot > 0:
            fatores.append([i, pot])  # adiciona lista, não sabia que dava para fazer isso
    return fatores

print(fatores_primos(1024))
