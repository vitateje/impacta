from typing import List

__alunos__ = ['gabriel.neves@aluno.faculdadeimpacta.com.br',
              'vitor.teixeira@aluno.faculdadeimpacta.com.br']


class Pessoa:
    '''
    Abstração de pessoa:
    '''
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade


class Funcionario(Pessoa):
    '''
    Classe Abstrata funcionário.
    '''
    def __init__(self, nome, idade, carga_horaria, valor_hora):
        super().__init__(nome, idade)
        self.carga_horaria = carga_horaria
        self.valor_hora = valor_hora
        self.salario = 0

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do Mês para o funcionário
        '''
        self.salario = self.valor_hora * self.carga_horaria
        return self.salario * 4.5

    def altera_carga_horaria(self, nova_carga_horaria: int) -> None:
        '''
        altera a carga horária do funcionário, respeitando o limite,
        de horas por categoria.
        Caso o numero informado seja inválido, da raise em um ValueError
        '''
        if nova_carga_horaria >= 16 and nova_carga_horaria <= 40:
            self.carga_horaria = nova_carga_horaria
        else:
            raise ValueError('Numero Invalido')

    def consulta_carga_horaria(self) -> int:
        '''
        Devolve a carga horária de trabalho do funcionário
        '''
        return self.carga_horaria

    def aumenta_salario(self) -> None:
        '''
        Da um aumento de 5% no valor da hora trabalhada para o funcionário
        '''
        self.valor_hora *= 1.05
        return self.valor_hora


class Programador(Funcionario):
    '''
    Funcionário do tipo programador, salario base por hora 35,00.
    Regime de trabalho deve estar entre 20 e 40h semanais,
    caso contrário devolve um ValueError.
    Para efeito de cálculo de pagamento o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 40, valor_hora: float = 35.00):
        super().__init__(nome, idade, carga_horaria_semanal, valor_hora)
        self.email = email
        if carga_horaria_semanal > 19 and carga_horaria_semanal < 41:
            self.carga_horaria = carga_horaria_semanal
        else:
            raise ValueError('Carga Horaria Invalida')
        self.salario = 0

    def altera_carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria > 19 and nova_carga_horaria < 41:
            self.carga_horaria = nova_carga_horaria
        else:
            raise ValueError('Numero Invalido')


class Estagiario(Funcionario):
    '''
    Funcionário do tipo estagiário, salario base por hora 15,50
    e auxilio alimentação de 250 reais por mês.
    Regime de trabalho deve estar entre 16h e 30h semanais,
    caso contrário da raise em um ValueError.
    Para efeito de cálculo de salário o mês possui 4,5 semanas
    '''
    def __init__(self, nome: str, idade: int, email: str,
                 carga_horaria_semanal: int = 20, valor_hora=15.50):
        super().__init__(nome, idade, carga_horaria_semanal, valor_hora)
        self.email = email
        if carga_horaria_semanal > 15 and carga_horaria_semanal < 31:
            self.carga_horaria = carga_horaria_semanal
        else:
            raise ValueError('Carga Horaria Invalida')
        self.salario = 0

    def altera_carga_horaria(self, nova_carga_horaria):
        if nova_carga_horaria > 15 and nova_carga_horaria < 31:
            self.carga_horaria = nova_carga_horaria
        else:
            raise ValueError('Numero Invalido')

    def calcula_salario(self) -> float:
        '''
        Calcula o salário do Mês para o funcionário
        '''
        self.lista_salario = []
        self.salario = ((self.valor_hora * self.carga_horaria) * 4.5) + 250
        return (self.salario)


class Empresa(Funcionario):
    '''
    Classe empresa, gerencia diversos funcionários
    '''
    def __init__(self, nome: str, cnpj: int, area_atuacao: str,
                 equipe: List[Funcionario] = []):
        self.nome = nome
        self.equipe = equipe
        self.cnpj = cnpj
        self.area_atuacao = area_atuacao

    def contrata(self, novo_funcionario: Funcionario) -> None:
        '''
        Contrata um novo funcionário para a empresa
        '''
        self.equipe.append(novo_funcionario)
        # pass

    def lista_fucionarios(self) -> List[Funcionario]:
        '''
        Devolve um lista com todos os funcionarios
        '''
        return self.equipe

    def folha_pagamento(self) -> float:
        '''
        Devolve o montante total gasto com pagamento dos funcionários
        '''
        soma=0
        for func in self.equipe:
            soma += func.calcula_salario()
        return soma

    def dissidio_anual(self) -> None:
        '''
        Aumenta o valor da hora trabalhada em 5% para todos os funcionários
        '''
        for func in self.equipe:
            func.aumenta_salario()

# testes#


if __name__ == '__main__':
    vitor = Estagiario('Vitor', 30, 'lucas@tex')
    print(vitor.consulta_carga_horaria())
    print(f'Carga horaria de Lucas {vitor.carga_horaria}')
    vitor.altera_carga_horaria(20)
    print(vitor.carga_horaria)
    vitor.calcula_salario()
    print(vitor.calcula_salario())
    print(vitor.aumenta_salario())
    print(vitor.calcula_salario())
    print(vitor.consulta_carga_horaria())
    tec = Empresa('Tec', 111000, 'Tecnologia', 'Time: TEC CRZ')
    tec.contrata(vitor.nome)
    tec.contrata('Fabio')
    tec.contrata('Maria')
    print(tec.equipe)
    print(tec.lista_fucionarios())
