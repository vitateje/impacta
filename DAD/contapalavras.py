def contardi(frase):
    partes = frase.split(' ')
    dic = {}
    for p in partes:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1
    return dic

print(contardi('esse exercício é um exercício fácil ou dificil'))
print(contardi('o doce perguntou ao doce qual é o doce mais doce e o doce respondeu ao doce que o doce mais doce é o doce de batata doce'))