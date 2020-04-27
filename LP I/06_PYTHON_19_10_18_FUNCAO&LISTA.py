#AULA FUNÇÃO:

def peso (p1,p2):
    p1=p1
    p2=p2
    media = (p1+p2)/2
    while p1 <= 0:
        p1=float(input('Digite novamente seu peso: '))
    return media

print(peso(15,14))

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO UM NUMERO NATURAL N (N>=O)
e devolva de divisores de n. '''

#AULA FUNÇÃO ex 04

def qtd_div(n):
    qtd=0
    for div in range(1, n+1):
        if n % div == 0:
            qtd += 1
    return qtd

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO UM NUMERO NATURAL N
e devolva um valor booleano indicando se n é primo. '''

#AULA FUNÇÃO ex 05

def primo(n):
    if qtd_div(n) == 2:
        return True
    else:
        return False

def aluno(n):
    return qtd_div(n) == 2

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO UM NUMERO NATURAL N
e devolva um valor booleano indicando se n é primo. '''

print('Hello World')

#AULA FUNÇÃO ex 06

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO DOIS NUMEROS NATURAIS i E f
(I<=F).'''

def inter_primo(i,f):
    for i in range(i, f+1):
        if primo(i):
            print(i)

#AULA FUNÇÃO ex 07

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO DOIS NUMEROS NATURAIS i E f
(I<=F).'''

def inter_primo(i,f):
    for i in range(i, f+1):
        if primo(i):
            print(i)

''' CRIE UMA FUNÇAO QUE RECEBA COMO PARAMETRO DOIS NUMEROS NATURAIS i E f
(I<=F) e devolva a soma dos primos do intervalo[i,f].'''

def soma_primos(i,f):
    s=0
    for i in range(i, f+1):
        if primo(i):
            s += i
    return s

#LISTAS

A=[1,2,3,4]

lista=[] #lista vazia
lista=['olá',1,8.5,True] #diferente elementos
lista.append(777) #adiciona no final
len(lista) #conta numeros da lista

print(lista[3]) #indice #indexando

lista[0]='Hello'
lista[2] += 12.5 #soma e atribui
lista.insert(3,False)
del lista[5]
lista.reverse()#inverte os valores
# lista.sort() #ordena os valores

print(lista)

#teste
def media(lista, n):
    s=0
    for i in range(n):
        s += lista [i]
    return s/n

qtd=int(input('Quantas ACs?'))
lista=[]
for i in range(qtd):
               x=float(input('Qual a nota?'))
               lista.append(x)
print(lista)
print(media(lista,qtd))

'''
════════════════════════════════════════════════════════════════════════════════
 Instituição  :  Faculdade Impacta Tecnologia
 Curso        :  Análise e Desenvolvimento de Sistemas
 Disciplina   :  Linguagem de Programação 1
 Turma        :  1B (noite)
 Professor    :  Lucio Nunes de Lira
 Aluno (1)    :  Vitor Tadeu Teixeira de Jesus
 Aluno (2)    :  Gleyver Coutinho Castro
 Matrícula (1):  1801745    
 Matrícula (2):  1801886
 Entrega      :  19/10/2018
════════════════════════════════════════════════════════════════════════════════
 Programa     :  AC7 (funções e listas)
════════════════════════════════════════════════════════════════════════════════
'''

'''─────────────────────────────────────────────────────────────────────────────
[ENUNCIADO]
  Crie uma função que receba dois números naturais como parâmetros, início e
  fim, que representam o intervalo inteiro [inicio,fim]. A função deverá cons-
  truir uma lista com todos os valores primos de início até fim e devolvê-la
  como resposta.

[RESTRIÇÕES]
  a) Usar apenas recursos vistos em nossas aulas;
  b) Usar apenas um laço de repetição, o mais adequado;
  c) Não usar funções prontas da linguagem para os cálculos;
  d) Obrigatório usar a função primo() feita em aula.

[ENTREGA]
  a) Equipe de dois alunos da mesma turma;
  b) Um dos integrantes poderá ser sorteado para explicar trechos do código;
  c) Serão consideradas apenas entregas dentro do prazo.

[CORREÇÃO]
  a) Notas baseadas na correção do código e explicação do membro sorteado;
  b) Caso sejam detectadas cópias, todas serão anuladas.
─────────────────────────────────────────────────────────────────────────────'''

def divisores(n):
    qtd = 0
    for i in range(1, n+1):
        if n % i == 0:
            qtd += 1
    return qtd

def primo(n):
    return divisores(n) == 2
  
def intprimo(n1,n2):
   
    lista=[]
    for cont in range(n1,n2+1,1):
        if primo(cont):
            s = cont
            lista.append(s)
    return lista       














     

    
    


    
        
        
