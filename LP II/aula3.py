def divisores(n):
    lista = []
    for i in range(1, n):
        if n % i == 0:
            lista.append(i)
    return lista


print(divisores(28))


def eh_perfeito(n):
    soma = sum(divisores(n))
    if soma == n:
        return True
    else:
        return False


print(eh_perfeito(28))


def lista_perfeitos(n):
    lista = []  # so cria a variavel quando precisar dela#
    for i in range(1, n):
        if eh_perfeito(i):
            lista.append(i)
    return lista


print(lista_perfeitos(0))
