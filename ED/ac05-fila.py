# Nome e R.A. da pessoa 1
# Nome e R.A. da pessoa 2 (se feito em dupla)


'''
EXPLICAÇÃO
Uma fila é uma estrutura de dados que tem um "início" (ou "frente") e um
"fim"

Ela guarda quantos elementos quisermos, mas só podemos ver/retirar
o elemento do início (frente).

Quando adicionamos um elemento, adicionamos no fim.

Em uma fila a operação "colocar no fim" é chamada de "inserir"
ou "enfileirar" (em inglês: "enqueue"),
e a operação "remover do início" é chamada simplesmente de "remover"
ou "desenfileirar" (em inglês: "dequeue").

Por exemplo:
    Criamos uma fila vazia.
    Se fizermos fila.insere(110), teremos a fila [110] (contém só o 110)
    Se fizermos fila.insere(209), fila.insere(58), teremos [110,209,58] (58 no fim, 110 no início)
    Se fizermos fila.remove(), saiu o início (110), e sobrou [209, 58]
'''

'''
EXERCÍCIO 1(a)
Continuando o exemplo, a fila está com [209, 58].

Digamos que fazemos fila.insere(87), fila.insere(270). Como está a fila? 
Responda preenchendo a fila abaixo (no momento tratamos como uma lista normal
do Python).
'''
fila1=[209, 58, 87, 270] # preencha com todo o conteúdo após a sequência de operações

'''
EXERCÍCIO 1(b)
Novo exemplo. Temos a fila vazia []
Fazemos fila.insere(9),fila.insere(8),fila.remove(),fila.insere(7),
fila.insere(6),fila.remove(). 

Como está a fila? Responda na variável fila2 abaixo.
'''
fila2=[7,6] # preencha com todo o conteúdo após a sequência de operações

'''
EXERCÍCIO 1(c)
Temos a fila [ 'Maria', 'João', 'Carlos', 'Débora' ].
Se fizermos algo como:

proximo = fila.frente()

Para obter a pessoa que está no início da fila, qual será o valor da
variável proximo? Preencha abaixo.
'''

proximo = 'Maria' # troque pelo valor correto

'''
EXPLICAÇÃO

Na prática, vamos implementar fila criando uma NOVA CLASSE.
Internamente, essa classe utiliza o tipo "deque", da biblioteca "collections"
do Python.

O "insere" é implementado usando o "append" do deque. É exatamente igual ao
append de uma list.

O "remove" usa o "popleft" do deque. É similar ao pop da lista,  mas ele remove
do INÍCIO em vez de remover do FIM.


A implementação abaixo é PARCIAL, não contém tudo que a fila precisa ter.
'''

from collections import deque

class Fila:
    def __init__(self):
        self.fila = deque() # atributo fila é um objeto do tipo deque

    def insere(self, novo):
        self.fila.append(novo) # uso append para inserir no final

    def remove(self):
        return self.fila.popleft() # popleft remove da esquerda (início)

    def tamanho(self):
        return len(self.fila) # usa len para calcular tamanho da fila

    def vazia(self):
        if len(self.fila) == 0:
            return True
        else:
            return False

'''
EXERCÍCIO 2

Faça a variável "minha_fila" receber um novo objeto da classe Fila.
'''

minha_fila = Fila() # troque pela instanciação

'''
EXERCÍCIO 3

Faça uma sequência de chamadas aos métodos da classe fila para INSERIR
em minha_fila os elementos
'cachorro'
'abacate'
'mesa'

Nessa ordem.
'''

minha_fila.insere('cachorro')
minha_fila.insere('abacate')
minha_fila.insere('mesa')

'''
EXERCÍCIO 4

Crie uma nova fila, chamada "nova_fila", e faça a seguinte sequência de
operações:
insere 19
insere 7
remove
insere 98
remove
insere 4
'''

nova_fila = Fila() # troque None pela criação do objeto
# faça as operações
nova_fila.insere(19)
nova_fila.insere(7)
nova_fila.remove()
nova_fila.insere(98)
nova_fila.remove()
nova_fila.insere(4)


'''
EXERCÍCIO 5

Crie na classe Fila um método "vazia", que retorna True, se a fila está vazia,
e False, caso contrário.

Exemplo de uso:
fila = Fila()
fila.vazia() --> retorna True
fila.insere(10)
fila.vazia() --> retorna False
'''

'''
EXERCÍCIO 6

Escreva uma função que insere vários elementos em uma fila.

Sua função recebe uma LISTA de elementos.

Ela deverá criar uma nova fila e inserir nela todos os elementos da lista,
em ordem.

Ao final, sua função irá retornar a fila criada.

Exemplo de comportamento:
insere_varios([1,2,3]) --> retorna fila contendo 1, 2, 3

'''

def insere_varios(lista):
    lista_ordem = Fila()
    for x in lista:
        lista_ordem.insere(x)
    return lista_ordem


'''
EXERCÍCIO 7

Escreva uma função que recebe uma fila e remove todos os seus itens,
guardando-os numa lista.

Ao final, sua função retorna essa lista.

Exemplo de comportamento:
f = Fila()
f.insere(10)
f.insere('oi')
remove_todos(f) --> retorna [10, 'oi']
f.vazia() --> retorna True

'''

def remove_todos(fila):
    deletados = []
    while fila.tamanho() != 0:
        #if fila.vazia() is False:
    
    #for x in fila:
        #fotografa(deletados)
        dele = fila.remove()
        deletados.append(dele)
    return deletados

'''
EXERCÍCIO 8

Vamos simular uma situação de fila no terminal de ônibus.
Escreva uma função que recebe uma LISTA DE NOMES (strings) que indica a ordem de
chegada das pessoas para pegar um ônibus no terminal.

Sua função deverá criar uma fila e inserir as pessoas nela, por ordem de chegada
(ordem em que aparecem na lista recebida como parâmetro).

Cuidado: existe um passageiro, chamado Samuel, que causou problemas no terminal
ontem. Hoje, o fiscal irá impedi-lo de embarcar, para que ele preste
esclarecimentos.

OU SEJA: você vai adicionar os nomes na fila, mas deverá ignorar o
Samuel, que não é autorizado a embarcar.


Depois, removendo um por um da fila, crie uma nova lista que mostra a ordem
em que as pessoas entrarão no ônibus.

Sua função irá, ao final, retornar a lista de embarque.

Exemplos:
embarca(['Jose', 'Henrique', 'Carla'])
--> retorna a lista [ 'Jose', 'Henrique', 'Carla' ], indicando a ordem de
embarque.

embarca(['Jose', 'Samuel', 'Carla'])
--> retorna a lista ['Jose', 'Carla']
'''

def embarca(pessoas):
    fila = Fila()
    #deletados = []
    for x in pessoas:
        if x == "Samuel":
            pass
        else:
            #fotografa(fila)
            fila.insere(x)
            fotografa(fila)  
          
    deletados = []
    while fila.tamanho() != 0:
        #if fila.vazia() is False:
    
    #for x in fila:
        #fotografa(deletados)
        dele = fila.remove()
        fotografa(fila)
        deletados.append(dele)
    return deletados


'''
EXERCÍCIO 9

Para garantir que você está no espírito da AC e portanto utilizando a classe
Fila para fazer a função embarca, modifique sua função embarca para que
ela tire fotografias (snapshots) da fila ao longo da execução.

Tire uma fotografia da sua fila após cada vez que você fizer uma inserção
ou remoção na fila.

Lembre-se que para tirar uma fotografia, você tem que fazer uma chamada do tipo:
fotografa(fila)

'''

'''
EXERCÍCIO 10

Vamos agora simular entrada de pessoas em um bar.

Faça uma nova função, entrada_bar.
Assim como a função anterior, ela recebe uma lista com a ordem de chegada
das pessoas.

Porém, agora, cada item da lista, em vez de ser uma string, é uma TUPLA
(nome, idade) que informa o nome e a idade da pessoa.

Exemplo: [ ('Jorge', 22), ('Melissa', 41), ('Fernando', 17), ('Laura', 27)  ]

Sua função deve retornar uma nova lista indicando a ordem de entrada das
pessoas, sendo que menores de idade são IMPEDIDOS de entrar.

Sua lista conterá apenas os NOMES.

Exemplo:
entrada_bar([ ('Jorge', 22), ('Melissa', 41), ('Fernando', 17), ('Laura', 27)  ])
--> retorna [ 'Jorge', 'Melissa', 'Laura' ]


'''
def entrada_bar(pessoas):
    #entrantes = Fila()
    teste = []

    for x in pessoas:
        if x[1] < 18:
            pass
        else:
            teste.append(x[0])
    return teste

#teste
# pessoas = [ ('Jorge', 22), ('Melissa', 41), ('Fernando', 17), ('Laura', 27)  ]
# teste = entrada_bar(pessoas)
# print(teste)

'''
EXERCÍCIO 11

Vamos agora fazer uma função que simula fila de banco.

Como no exercício anterior, sua função irá receber uma lista de tuplas, onde
cada tupla contém (nome, idade) de uma pessoa.

Exemplo de lista: [ ('Jorge', 22), ('Luiza', 67), ('Carlos', 40) ]

As pessoas com menos de 60 anos entram na fila normal.
As pessoas com 60 anos ou mais entram na fila prioritária.

Hoje só um caixa está funcionando. Para que os idosos sejam atendidos com
rapidez, o caixa está fazendo o seguinte: a cada vez, ele chama DUAS pessoas
da fila prioritária (se existirem), e então UMA pessoa da fila normal.

Sua tarefa é escrever uma função que recebe a lista de pessoas e retorna
uma lista com os nomes dos clientes na ordem em que são atendidos.

Exemplos de comportamento:
fila_banco([ ('Jorge', 22), ('Luiza', 67), ('Carlos', 40) ])
--> retorna ('Luiza', 'Jorge', 'Carlos')

fila_banco([ ('Jorge', 22), ('Valter', 90), ('Alice', 88), ('Boris', 77) ])
--> retorna ('Valter', 'Alice', 'Jorge', 'Boris')


'''

def fila_banco(pessoas):
    fila_geral = []
    teste = []
    fila_normal = Fila()
    fila_idoso = Fila()
    for x in pessoas:
        if x[1] > 60:
            fila_idoso.insere(x[0])
            fotografa(fila_idoso)
        else:
            fila_normal.insere(x[0])
            fotografa(fila_normal)
    b = []
    tamanho_lista = fila_idoso.tamanho()
    for i in range(len(pessoas)):
        if fila_idoso.tamanho() != 0:
            # if (indice )
            a = fila_idoso.remove()
            fotografa(fila_idoso)
            fila_geral.append(a)
            b.append(a)
        if fila_normal != 0:
            if tamanho_lista == 1:
                try:
                    a = fila_normal.remove()
                    fotografa(fila_normal)
                    fila_geral.append(a)
                    b.clear()
                except:
                    pass
                
            if (len(b) == 2):
                pessoa_normal = fila_normal.remove()
                fotografa(fila_normal)
                fila_geral.append(pessoa_normal)
                b.clear()
    return fila_geral

# pessoas = [ ('Jorge', 22), ('Valter', 90), ('Alice', 88), ('Boris', 77) ]
# # ('Valter', 'Alice', 'Jorge', 'Boris')
# teste = fila_banco(pessoas)
# print(teste)

'''
EXERCÍCIO 12

Modifique a função fila_banco para que ela tire uma fotografia de cada uma das
filas (a normal e a prioritária) a cada inserção ou remoção.

'''

# FIM DA AC. O código abaixo é para os testes automatizados, além da
# implementação da função "fotografa".
# --------------------------------------------------------------------------
import unittest
import sys
import inspect
import hashlib


class TestStringMethods(unittest.TestCase):

    def test_01_vars_fila1_fila2_proximo(self):
        self.compara_hash(fila1, [209, 58, 87, 270])
        self.compara_hash(fila2, [7, 6])
        self.compara_hash(proximo, 'Maria')

    def test_02_var_minha_fila(self):
        self.assertTrue(type(minha_fila) is Fila)

    def test_03_operacoes_minha_fila(self):
        gabarito = deque()
        gabarito.append('cachorro')
        gabarito.append('abacate')
        gabarito.append('mesa')
        self.assertEqual(minha_fila.fila, gabarito)

    def test_04_nova_fila(self):
        self.assertTrue(type(nova_fila) is Fila)
        gabarito = deque()
        gabarito.append(19)
        gabarito.append(7)
        gabarito.popleft()
        gabarito.append(98)
        gabarito.popleft()
        gabarito.append(4)
        self.assertEqual(nova_fila.fila, gabarito)
        
    
    def test_05_fila_vazia(self):
        teste = Fila()
        self.assertEqual(teste.vazia(), True)
        teste.insere(0)
        self.assertEqual(teste.vazia(), False)
        teste.remove()
        self.assertEqual(teste.vazia(), True)

    def test_06_insere_varios(self):
        teste = Fila()
        self.assertEqual(insere_varios([]).fila, teste.fila)
        teste.insere(1)
        teste.insere(2)
        teste.insere('a')
        self.assertEqual(insere_varios([1,2,'a']).fila, teste.fila)

    def test_07_remove_todos(self):
        teste = Fila()
        self.assertEqual(remove_todos(teste), [])
        teste.insere(1)
        teste.insere(2)
        teste.insere('a')
        self.assertEqual(remove_todos(teste), [1,2,'a'])


    def test_08_embarca(self):
        self.assertEqual(embarca(['Jose', 'Henrique']), ['Jose', 'Henrique'])
        self.assertEqual(embarca([]), [])
        self.assertEqual(embarca(['Samuel']), [])
        self.assertEqual(embarca(list(range(10))), list(range(10)))
        self.assertEqual(embarca(list(range(10)) + ['Samuel'] + list(range(100))), list(range(10)) + list(range(100)))


    def test_09_embarca_fotos(self):
        reseta_fotos()
        embarca(['Jose', 'Henrique'])
        album_correto = []
        album_correto.append(deque(['Jose']))
        album_correto.append(deque(['Jose', 'Henrique']))
        album_correto.append(deque(['Henrique']))
        album_correto.append(deque([]))
        album_dado = fotografias
        
        if (album_correto != album_dado):
            print('Função embarca não tirou as fotografias corretas')
            explica_erro(album_dado, album_correto)
            self.fail('Erro nas fotografias')


    def test_10_entrada_bar(self):
        self.assertEqual(entrada_bar([]), [])
        pessoas = [ ('a', 10) ]*5 + [('x', 18), ('y', 20)]*2
        self.assertEqual(entrada_bar(pessoas), ['x', 'y']*2)
    
    def test_11_fila_banco(self):
        exemplo1 =  [('Jorge', 22), ('Valter', 90), ('Alice', 88), ('Boris', 77)]   
        self.assertEqual(fila_banco(exemplo1), ['Valter', 'Alice', 'Jorge', 'Boris'])
        exemplo2 = [ ('Jorge', 22), ('Luiza', 67), ('Carlos', 40) ]
        self.assertEqual(fila_banco(exemplo2), ['Luiza', 'Jorge', 'Carlos'])

    def test_12_fila_banco_fotos(self):
        reseta_fotos()
        fila_banco([('Breno', 19), ('Jose', 63), ('Henrique', 71)])
        album_correto = []
        album_correto.append(deque(['Breno']))
        album_correto.append(deque(['Jose']))
        album_correto.append(deque(['Jose', 'Henrique']))
        album_correto.append(deque(['Henrique']))
        album_correto.append(deque([]))
        album_correto.append(deque([]))
        album_dado = fotografias
        
        if (album_correto != album_dado):
            print('Função fila_banco não tirou as fotografias corretas')
            explica_erro(album_dado, album_correto)
            self.fail('Erro nas fotografias')


    def compara_hash(self, elemento1, elemento2):
        codigo1 = hashlib.sha224(str(elemento1).encode('utf-8')).hexdigest()
        codigo2 = hashlib.sha224(str(elemento2).encode('utf-8')).hexdigest()
        self.assertEqual(codigo1, codigo2)
        

def runTests(rapido = False):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=rapido).run(suite)


fotografias = []
def reseta_fotos():
    global fotografias
    fotografias = []

def fotografa(elemento):
    try:
        copia = elemento.fila.copy()
        fotografias.append(copia)
    except:
        fotografias.append(elemento)
        
def explica_erro(album1,album2):

    print('')

    if len(album1) == 0 and len(album2) > 0:
        print('Você não tirou nenhuma fotografia')
        print('Primeira fotografia esperada:')
        print(album2[0])
        return

    
    tam_do_menor = min(len(album1),len(album2))
    diferentes = [i for i in range(tam_do_menor) if album1[i] != album2[i]]
    if len(diferentes) > 0:
        menor_diferente = min(diferentes)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('Sua primeira fotografia errada:')
        print(album1[menor_diferente])
        print('Era esperado:')
        print(album2[menor_diferente])
        return

    if len(album1) < len(album2):
        print('Você tirou fotografias a menos')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album1)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que faltou:')
        print(album2[menor_diferente])

    if len(album1) > len(album2):
        print('Você tirou fotografias a mais')
        print('Voce tirou '+str(len(album1))+ ' fotografias, mas era pra tirar ' + str(len(album2)))
        menor_diferente = len(album2)
        print('Suas primeiras ' + str(menor_diferente) + ' fotografias estao certas')
        print('Suas fotografias corretas:')
        for j in range(menor_diferente):
            print(album1[j])
        print('A primeira fotografia que sobrou:')
        print(album1[menor_diferente])

#---------------------------------------------------------------------------
# para SEMPRE rodar os testes, descomentar uma das linhas de  código abaixo:

# roda TODOS os testes:
#runTests()

# roda só até a primeira falha:
runTests(rapido = True)

