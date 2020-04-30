__alunos__ = ["email_aluno_1",
              "email_auno2"]

import auxiliares as aux


def acha_mais_frequente(dicionario):
    maior = 0
    freq = ''
    for palavra in dicionario:
        if dicionario[palavra] > maior:
            maior = dicionario[palavra]
            freq = palavra
    return [freq, maior]


def conta_palavra_por_livro():
    """
    Devolve um Dicionário Python onde cada chave é o nome de um livro
    da Bíblia e o valor associado é um lista com a palavra mais frequente
    e o número de ocorrências da palavra.
    """

    lista_dicionarios = []
    for linha in aux.le_biblia():
        if aux.eh_novo_livro(linha):
            lista_dicionarios.append({})
        else:
            for palavra in linha.split():
                if palavra in lista_dicionarios[-1]:
                    lista_dicionarios[-1][palavra] += 1
                else:
                    lista_dicionarios[-1][palavra] = 1

    mais_frequentes = {}

    for i, dicionario in enumerate(lista_dicionarios):
        mais_frequentes[i+1] = acha_mais_frequente(dicionario)

    return mais_frequentes
