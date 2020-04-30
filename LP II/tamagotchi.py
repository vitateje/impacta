''' Da Wikipedia, temos: “O Tamagotchi é um brinquedo em
que se cria um animal de estimação virtual. O tamagotchi
foi lançado pela Bandai em 1996 no Japão. A motivação do
brinquedo consiste em cuidar do animalzinho virtual como
se fosse real, dando-lhe carinho virtual, comida virtual,
banho virtual, cuidados virtuais etc.”Implemente uma
versão simplificada do jogo conforme especificado no
arquivo em anexo.Você deverá também implementar um
arquivo de testes (no formato pytest) para verificar
sua implementação. Envie esse arquivo junto com sua
implementação na entrega da tarefa '''

from typing import Dict

__aluno__ = ""


class Tamagotchi:
    '''
    Abstração de um bichinho virtual
    * recebe como atributos no construtor: nome e dono, deverão ser atributos
    públicos
    * além disso deve ter os atributos: vidas, total_de_vidas, energia e
    energia_total (todos privados)
    * o total_de_vidas deverá ser 7 e a energia_total deverá ser 100
    '''
    def __init__(self, name: str, dono: str):
        self.name = name
        self.dono = dono
        self._vidas = 7
        self._total_de_vidas = 7
        self._energia = 100
        self._total_de_energia = 100

    def consulta_energia(self) -> int:
        '''
        Devolve a energia atual do Tamagotchi
        '''
        return self._energia

    def altera_energia(self, valor: int) -> None:
        '''
        Soma o valor, que pode ser negativo ou positivo à energia do Tamagochi
        * Caso a nova energia ultrapasse a energia total, ele deverá limitar a
        energia na energia total
        * Caso a nova energia fique menor que zero, a energia deverá ter seu
        valor mudado para 100 e deverá ser retirada 1 vida do Tamagochi.
        * Caso o Tamagotchi chegue a 0 vidas, deverá retornar uma Exception
        com a mensagem 'Game Over'
        '''
        self._energia += valor
        if self._energia > self._total_de_energia:
            self._energia = self._total_de_energia
        elif self._energia <= 0:
            self._energia = self._total_de_energia
            self._vidas -= 1
            if self._vidas <= 0:
                raise Exception('Game Over')

    def status(self) -> Dict:
        '''
        Retorna um dicionário com o estado atual do seu tamagochi:
        * as chaves do dicionário deverão ter o mesmo nome dos atributos do
        tamagotchi trocando o caracter '_' por espaço.
        exemplo de saída: {'nome': 'Rex', 'dono': 'Guilheme',
                           'energia total': 100, 'energia': 70,
                           'total de vidas': 7, 'vidas' 3}
        '''
        return  {'nome': self.name, 'dono': self.dono,              "energia total": self._total_de_energia,
                'energia': self._energia,
                'total de vidas': self._total_de_vidas,
                'vidas': self._vidas}


class TamagotchiDinossauro(Tamagotchi):
    '''
    Abstração de um Tamagotchi Dinossauro
    * Sua energia total deverá ser 150 e seu total de vidas 5
    * A mensagem da exceção caso ele atinja 0 vidas deverá ser "Extinto"
    '''
    def __init__(self, name, dono):
        super().__init__(name, dono)
        self._vidas = 5
        self._total_de_vidas = 5
        self._energia = 150
        self._total_de_energia = 150

    def altera_energia(self, valor: int) -> None:
        self._energia += valor
        if self._energia > self._total_de_energia:
            self._energia = self._total_de_energia
        elif self._energia <= 0:
            self._energia = self._total_de_energia
            self._vidas -= 1
            if self._vidas == 0:
                raise Exception('Extinto')


class TamagotchiCachorro(Tamagotchi):
    '''
    Abstração de um Tamagotchi Cachorro
    * Sua energia total deverá ser 80 e seu total de vidas 10.
    * A mensagem da exceção caso chegue a 0 vidas deverá ser "foi para um lugar
    melhor"
    '''
    def __init__(self, name, dono):
        super().__init__(name, dono)
        self._vidas = 10
        self._total_de_vidas = 10
        self._energia = 80
        self._total_de_energia = 80

    def altera_energia(self, valor: int) -> None:
        self._energia += valor
        if self._energia > self._total_de_energia:
            self._energia = self._total_de_energia
        elif self._energia <= 0:
            self._energia = self._total_de_energia
            self._vidas -= 1
            if self._vidas == 0:
                raise Exception('Extinto')


''' TESTES UNITARIOS '''

if __name__ == "__main__":

    Bili_Joel = TamagotchiDinossauro('Bili Joel', 'Leka')
    Croc_No_Rivers = TamagotchiCachorro('Croc No Rivers', 'Black Flowers')
    Bili_Joel.altera_energia(-30)
    print(Bili_Joel.consulta_energia())
    print(Bili_Joel.status())

    '''print(f'Status: {Croc_No_Rivers.status()}')
    print(f'Status: {Bili_Joel.status()}')
    Bili_Joel.altera_energia(-100)
    Croc_No_Rivers.altera_energia(-49)
    Bili_Joel.altera_energia(-100)
    print(f'Status: {Bili_Joel.status()}')
    Bili_Joel.altera_energia(-99)
    Bili_Joel.altera_energia(-1)
    Croc_No_Rivers.altera_energia(-1)
    Bili_Joel.altera_energia(-13)
    print(f'Status: {Bili_Joel.status()}')'''
