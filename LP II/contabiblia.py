import auxiliares as aux


palavras = {}

for linha in aux.le_biblia():
    for palavra in linha.split():
        if palavra in palavras:
            palavras[palavra] += 1
        else:
            palavras[palavra] = 1

maior = 0
freq = ''
for palavra in palavras:
    if palavras[palavra] > maior:
        maior = palavras[palavra]
        freq = palavra

print(freq, maior)
