'''
Ao longo do código abaixo, há uma série de exercícios.
Alguns aparecem fora de ordem porque existem exercícios dentro e fora doc
código da classe
'''

# classe Dominó ----------------------------------------------------------------
class Domino:
    def __init__(self, ponta1, ponta2):
        self.ponta1 = ponta1
        self.ponta2 = ponta2

    # o método encaixa recebe outra peça de dominó como parâmetro
    # e retorna True, se as duas peças encaixam
    def encaixa(self, outro):
        return (self.ponta2 == outro.ponta1)
   
    # o método abaixo retorna True, se a peça de dominó for dupla (ou "bucha")
    # exemplo: peça 6/6, peça 2/2, etc.
    def duplo(self):
        return (self.ponta1 == self.ponta2)
     
    ''' Exercício 3:
        escreva um método que retorna True, se a peça é válida, e False,
        caso contrário.
    
        uma peça é VÁLIDA se, e somente se, suas duas pontas têm valor de
        0 (zero, isto é, a peça branca) até 6 (seis).
        
        Exemplos:
            * pontas -1 e 3 --> não é válida
            * pontas 5 e 5 --> válida
            * pontas 4 e 8 --> não é válida
            * pontas 2 e 0 --> válida
    '''
    def valida(self):
        lista = [0,1,2,3,4,5,6]
        if self.ponta1 in lista and self.ponta2 in lista:
            return True
        else:
            return False

    ''' Exercício 5:
        Escreva um método que retorna uma string
	representando a peça de dominó, de acordo com o exemplo:

	Peça com pontas 3 e 5: string '[ 3 | 5 ]'.
	Peça com pontas 0 e 2: string '[ 0 | 2 ]'.
    '''
    def mostra(self):
        return f"Peça com pontas {self.ponta1} e {self.ponta2}: string'[ {self.ponta1} | {self.ponta2} ]'."


    ''' Exercício 7:
        Escreva um método que gira a peça.
    '''
    def gira(self):
        if self.ponta1 != self.ponta2:
            ponta1 = self.ponta2
            ponta2 = self.ponta1
            self.ponta1 = ponta1
            self.ponta2 = ponta2

    
    
# -----------------------------------------------------------------------------

''' Exercício 1:

no exemplo abaixo, criamos uma peça de Dominó usando o construtor da classe
Dominó.

seguindo o exemplo, instancie (crie) outra peça, que encaixe nessa primeira
'''
peca_1 = Domino(1,1)

peca_2 = Domino(1,5)

print(peca_1.valida())


# Teste para ver se a peca_2 realmente encaixa:
# (tire o comentário para executar)
#print('Peça 1 e 2 encaixam? ---> ', peca_1.encaixa(peca_2))

'''Exercício 2:

Use uma chamada ao método 'dupla' para verificar se a peça 1 é dupla,
e mais outra chamada para verificar se a peça 2 é dupla.

Dê print no resultado!
'''
print(peca_1.mostra())
print(peca_1.duplo())
print(peca_2.duplo())

''' Exercício 3: (enunciado está no código da classe)
'''

''' Exercício 4:

Veja no exemplo abaixo como fazemos para criar uma lista de peças de 
dominó.

Chamaremos uma lista de peças de um JOGO.
'''

jogo = [ Domino(1, 2), Domino(2, 6), Domino(6, 6), Domino(6, 0) ]

'''
Seguindo o exemplo, crie uma lista de peças que seja um jogo correto
e uma lista de peças que seja um jogo incorreto

Um jogo é CORRETO se cada peça se encaixa com a seguinte.
Um jogo é INCORRETO caso alguma peça não se encaixe na seguinte.

'''
correto = [ Domino(3,4), Domino(4,6), Domino(6,5), Domino(5,3) ]
incorreto = [ Domino(3,5), Domino(4,2), Domino(1,5) ] 

''' Exercício 5: (enunciado está no código da classe)
'''

''' Exercício 6:
Escreva uma função que recebe um jogo (lista de dominós) e imprime todo
seu conteúdo.
'''

def imprime_jogo(jogo):
    for x in jogo:
        #x.gira() - teste ex 7
        print(x.mostra())

''' Exercício 7: (enunciado no código da classe)
'''

# Os exercícios 8 a 10 são opcionais! Desafios extras

''' Exercício 8:
Escreva uma função que recebe um jogo (lista de dominós) e retorna True,
se todas as peças são válidas, e False caso contrário.
'''


def valida_jogo(jogo):
    for x in jogo:
        if x.valida() is not True:
            return False
    return True

''' Exercício 9:
Escreva uma função que recebe um jogo (lista de dominós) e retorna True,
se a lista é um jogo correto. False caso contrário.
'''

# def jogo_correto(jogo):
#     for x in jogo:
#         item2 = 1
#         if x.ponta2 == jogo[item2].ponta1:
#             item2 += 1
#             print (True)
#     return f'False OO'

# print(jogo_correto(jogo))

''' Exercício 10:
Escreva uma função que recebe um jogo (lista de dominós) e retorna True,
se a lista é um jogo correto e circular (a última peça encaixa na primeira)
'''

