__alunos__ = ["email_aluno_1", "email_aluno2"]

import auxiliares as aux

def conta_palavra_por_livro():
    """
    Devolve um Dicionário Python onde cada chave é o nome de um livro
    da Bíblia e o valor associado é um lista com a palavra mais frequente
    e o número de ocorrências da palavra.
    """


livro = {}
palavras = {}
for linha in aux.le_teste():
    if aux.eh_novo_livro(linha):
        livro['1']=linha
        for linha in aux.le_teste():
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

#print(livro)
#print(palavras)
