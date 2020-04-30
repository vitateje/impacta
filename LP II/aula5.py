''' orientação a objetos - um paradigma para resolver/modelar um problema -
procedural , POO - Orientado a objetos e funcional.
modelagem com objetos - com caracteristicas e comportamentos/metodos
classe - classificação dos objetos - é o esquema/template
objeto é uma instancia de uma classe - vai obedecer o template e ter suas proprias caracteristicas
objeto = variavel = atributos / função = método '''


str.__add__

# toda variavel é um objeto

# POO - tem abstração - 

lista = list ()

inteiro=1
print(type(lista))

 #dic. chama os metodos

dic.items(chave)
print(dic)


''' correção orientação a objetos: AC02 
classe defini o comportamento e o atributo de um objeto '''

''' classe é um tipo de um objeto - croqui do objeto 
metodos - comportamento do objeto
atributos - caracteristicas do objeto
objeto - instancia de uma classe '''

# como declarar uma classe
class Televisao():  # () por causa da herança # classe é CamelCase
    pass # vazia

# como instanciar (criar) uma classe

tv_sala = Televisao()
tv_quarto = Televisao()

print(type(tv_sala))

# atributos, construtor e "self"


class Televisao() : 
    def __init__(self, marca_da_televisao, polegadas, cor_televisao):  # construtor
        self.marca = marca_da_televisao  # cria uma variavel no proprio objeto e recebe o parametro
        self.pol = polegadas  # construtor # criação dos atributos
        self.cor = cor_televisao  # default vai ser preto
        self.ligada = False



    def ligar(self):
        self.ligada = True # faz uma função que altera o estado do objeto ou devolve algo


class Dummy():
    def __init__(self):
        print('Olá Mundo')


tv_sala = Televisao ( 'samsung', 22, 'branca')
tv_quarto = Televisao ('AOC', 11,'branca')


tv_sala.ligar()
print(tv_sala.ligada) # = True

print(tv_sala.marca, tv_sala.pol+1, tv_sala.cor) #criação do objeto
print(tv_quarto.marca, tv_quarto.pol)

dummy=Dummy() #criação do objeto
dummy2=Dummy()
dummy3=Dummy()
dummy4=Dummy()

#implementação de metodos

#chamando ojbetos

#objetos como atributos