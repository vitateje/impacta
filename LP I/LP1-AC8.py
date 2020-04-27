'''═════════════════════════════════════════════════════════════════════════════
 Instituição  :  Faculdade Impacta Tecnologia
 Curso        :  Análise e Desenvolvimento de Sistemas
 Disciplina   :  Linguagem de Programação 1
 Turma        :  1B (noite)
 Professor    :  Lucio Nunes de Lira
 Aluno        :  
 Matrícula    :  
 Entrega      :  26/10/2018
════════════════════════════════════════════════════════════════════════════════
 Programa     :  AC8 e AC9 (funções, sequências e busca)
═════════════════════════════════════════════════════════════════════════════'''

'''─────────────────────────────────────────────────────────────────────────────
[1º ENUNCIADO]
  Crie uma função que receba como parâmetros um caractere C e uma string S e 
  devolva a quantidade de ocorrências de C em S.

[2º ENUNCIADO]
  Crie uma função que receba como parâmetros uma tupla de naturais T e um
  natural x e devolva uma lista com todos os itens de T divisíveis por x.

[3º ENUNCIADO]
  Crie uma função que receba como parâmetros um número real x, uma lista de 
  reais L e o tamanho n (n > 0) de L. A função deverá devolver um valor
  booleano indicando se existe em L um item menor que x.

[RESTRIÇÕES]
  a) Usar apenas recursos vistos em nossas aulas;
  b) Usar apenas um laço de repetição, o mais adequado;
  c) Não usar funções prontas da linguagem para os cálculos (exceto o len()).

[ENTREGA]
  a) Individual;
  b) Serão consideradas apenas entregas dentro do prazo.

[CORREÇÃO]
  a) Notas baseadas na correção do código;
  b) Caso sejam detectadas cópias, todas serão anuladas.
─────────────────────────────────────────────────────────────────────────────'''

# Quais funções foram escolhidas: [2] e [3] (somente duas).

def lista_div(t, x):
   lista = []
   for i in t:
       if i % x == 0:
           lista.append(i)
   return lista

def func3(x,L,n):
    for i in range(n):
        if L[i]<x:
            return True
    return False   
