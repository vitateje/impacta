''' REVISAO '''

''' TRATAMENTO DE ERROS - RAISE - EXCEPT '''

class Televisao():
    '''
    Classe que abstrai uma Televisao
    '''

    def __init__(self, marca: str, tamanho: float) -> None:  #  type para documentar (str float boolean)
        '''
        Construtor da Classe
        '''

        self.set_marca(marca) #set direto #chama a func e o parametro é o atributo
        self._tamanho = tamanho  # self caracteriza o atributo#
        self._antena = ['UHF', 'VHF']

    def get_marca(self):
        return self._marca

    def get_antena(self):
        return self._antena.copy()  # para dicionario e listas

    def set_marca(self, nova_marca: str) -> None:
        if type(nova_marca) == str:
            self._marca = nova_marca
        else:
            raise Exception('Marca deve ser uma string')#typeError #valueError
             #levanta um erro / tratamento de erro

    def set_tamanho(self, novo_tamanho: float) -> None:
        '''
        Setter para o atributo tamanho, se for menor que 0
        devolve ValueError.
        '''
        if not type(novo_tamanho) == float:
            raise TypeError('Tamanho deve ser float')
        if novo_tamanho <= 0:
            raise ValueError('Tamanho deve ser maior que 0')
        self._tamanho = novo_tamanho

    def get_tamanho(self):
        return self.get_tamanho



if __name__ == '__main__': # so roda nesse arquivo / modulo principal
    tv_sala = Televisao('LG', 22)
    a = tv_sala.get_tamanho()
    print(a)
    print(tv_sala.set_tamanho(5.5))
    print(tv_sala.get_antena())