lista = ['maça', 'iogurte', 'banana']

for index, item in enumerate(lista):
    print(index,item)

for i in range(len(lista)):
    print('índice', i, ':', lista[i])

# receba 3 parametros e retorne o maior

def maximo(x,y,z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    elif z > y and z > x:
        return z


print(maximo(3,50,9))

print(max(2,3,5))

lista1 = [0,2,6,9,5,13,55]

ordenada = sorted(lista1) # ordena lista

print(ordenada[-2]) # imprime o ultimo item da lista -1 (-2 antepenultimo)

#busca binaria tem que ser em lista ordenada
