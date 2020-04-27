'''
════════════════════════════════════════════════════════════════════════════════
 Instituição   :  Faculdade Impacta Tecnologia
 Curso         :  Análise e Desenvolvimento de Sistemas | Banco de Dados
 Disciplina    :  Linguagem de Programação 1
 Autor         :  Professor Lucio Nunes de Lira
════════════════════════════════════════════════════════════════════════════════
 Linguagem     :  Python 3
 Interpretador :  CPython (3.7)
 Versão        :  A (Rev. 0)
 Programa      :  Sorteio de alunos em equipes.
════════════════════════════════════════════════════════════════════════════════
'''

# Biblioteca com funções para randomização.
import random

# Inicialização do valor semente
# Obs.: Se omissão de parâmetro adota-se o tempo do sistema.
random.seed()

# Função que lê nomes e devolve uma equipe.
def equipe():
    eq = []
    integrante = input(' Integrante: ')
    while integrante != '':
        eq.append(integrante)
        integrante = input(' Integrante: ')
    return eq

# Constrói uma lista de equipes.
qtd_equipes = int(input('Quantidade de equipes: '))
equipes = []
for i in range(qtd_equipes):
    print('֎ Equipe %d' % (i+1))
    equipes.append(equipe())

# Sorteia e exibe um integrante por equipe.
print('Sorteados')
for i in range(qtd_equipes):
    print('֎ Equipe %d:' % (i+1), end=' ')
    sorteado = random.randint(0, len(equipes[i])-1) # [início,fim]
    print(equipes[i][sorteado])