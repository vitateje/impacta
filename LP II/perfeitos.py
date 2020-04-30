# import lp2aula1 <--serve para importar um módulo de um outro arquivo #
'''from lp2aula1 import ehprimo as a1
import numpy as np
import math

print(a1(33))
print(np.zeros(6))
print(math.pi)'''


def lista_divisores(n):
    lista = []
    for i in range(1, n):
        if n % i == 0:
            lista.append(i)
    return lista


def eh_perfeito(n):
    soma = sum(lista_divisores(n))
    if soma == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []
    for i in range(1, n+1):
        if eh_perfeito(i):
            lista.append(i)
    return lista


def lista_n_perfeitos(n):
    lista_n_perfeitos=[]
    i=2
    while len(lista_n_perfeitos) < n:
        if eh_perfeito(i):
            lista_n_perfeitos.append(i)
        i += 1    
    return lista_n_perfeitos


def lista_perfeitos_e_divisores(n): # done by myself
    lista=[]
    for i in range(1,n):
        if eh_perfeito(i):
            lista.append([i,lista_divisores(i)])
    return lista
