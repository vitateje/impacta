def lista (): #cria função com listas do mes
    mes30 = [4,6,9,11]
    mes31 = [1,3,5,7,8,10]
    mes28 = [2]
    lista = mes30 + mes28 + mes31
    return (lista)

lista=lista() #chama a função lista
print(lista)


for x in lista:
    if x == 4 or x == 6:
        print ('mes 30')