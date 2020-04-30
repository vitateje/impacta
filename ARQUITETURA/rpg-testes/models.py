class DefinicaoAtaque(object):
    def __init__(self, potencia, distancia, direcao):
        self.potencia = potencia
        self.distancia = distancia
        self.direcao = direcao
    
    def __str__(self):
        return f'atacando: pot: {self.potencia}, dis: {self.distancia}, dir: {self.direcao}'

class Personagem(object):
    @staticmethod
    def cria_personagem(classe):
        if classe == 'Guerreiro':
            return Guerreiro('Arthur', 100)
        if classe == 'Mago':
            return Mago('Merlin', 60)

        raise Exception('Tipo de personagem inválido')

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def ataque(self, direcao):
        return DefinicaoAtaque(int(self.vida/3), 1, direcao)

class Guerreiro(Personagem):
    pass

class Mago(Personagem):
    pass
