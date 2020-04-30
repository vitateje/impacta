__alunos__ = []

# getters - função que define como será visualizada a informação solicitada ()

# setters - função que define como será alterada a informação solicitada ()

import math as m


class Ponto():
    """
    Implementa uma abstração de um ponto no plano cartesiano 2D
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def desloca(self, x: float, y: float) -> None:
        self.x += x
        self.y += y

    def dist(self, ponto: 'Ponto') -> float:
        """
        Calcula a distância euclidiana entre o objeto e um outro ponto do
        plano cartesiano
        """
        d = (self.x - ponto.x) ** 2 + (self.y - ponto.y) ** 2
        return m.sqrt(d)


class Circulo():
    """
    Implementa uma abstração para um círculo no plano cartesiano 2D
    Você deverá checar se os tipos passados no construtor estão corretos
    e caso contrário devolver um ValueError.
    Você deverá checar se o raio é maior que 0 e em caso contrário devolver
    um ValueError
    """

    def __init__(self, centro: Ponto, raio: float) -> None:      
        '''
        Seu construtor deverá receber o centro do circulo e o raio,
        e guardá-los em atributos protegidas.
        '''
        if not type(raio) == float:
            raise TypeError('Valor deve ser Float')
        elif raio <= 0:
            raise ValueError('Valor deve ser maior que 0')
        self._raio = raio

        if not type(centro) == Ponto:
            raise TypeError('Não é do tipo Ponto')
        self._centro = centro
        

    def get_centro(self) -> Ponto:
        '''
        Acessor para o atributo centro do circulo
        '''
        return self._centro

    def set_centro(self, novo_centro: Ponto) -> None:
        '''
        Mutador para o atributo centro do circulo, Devolve um 
        TypeError caso o Tipo não esteja Correto.
        '''
        if not type(novo_centro) == Ponto:
            raise TypeError('Não é do tipo Ponto')
        self._centro = novo_centro

    def get_raio(self) -> float:
        '''
        acessor para o atributo raio do circulo
        '''
        return self._raio

    def set_raio(self, novo_raio: float) -> None:
        '''
        Mutador para o atributo raio do circulo.
        Deve retornar um Typer Erro Caso o Tipo não seja float.
        Caso o novo raio seja negativo deve acusar a exceção ValueError
        '''
        if not type(novo_raio) == float:
            raise TypeError('Valor deve ser Float')
        elif novo_raio <= 0:
            raise ValueError('Valor deve ser maior que 0')
        self._raio = novo_raio

    def area(self) -> float:
        """
        Calcula a área do Circulo
        """
        area = self._raio ** 2 * m.pi
        return area
    

    def perimetro(self) -> float:
        """
        Calcula o perímetro do Circulo
        """
        perimetro = self._raio * 2 * m.pi
        return perimetro


if __name__ == "__main__":
    ponto1 = Ponto(2.1,2.2)
    circ = Circulo(ponto1, -5.5)
