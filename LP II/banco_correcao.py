from typing import Union, List, Dict

Number = Union[int, float]

__alunos__ = ["email_aluno_1@aluno.faculdadeimpacta.com.br",
              "email_aluno_2@aluno.faculdadeimpacta.com.br"]


class Cliente():
    """
    Classe Cliente do Banco
    """
    def __init__(self, nome: str, telefone: int, email: str):
        self._nome = nome
        self.set_telefone(telefone)
        self.set_email(email)

    def get_nome(self) -> str:
        '''
        Acessor do atributo Nome
        '''
        return self._nome

    def get_telefone(self) -> int:
        '''
        Acessor do atributo Telefone
        '''
        return self._tel

    def set_telefone(self, novo_telefone: int) -> None:
        '''
        Mutador do atributo telefone, caso não recebe um número,
        retorna um TypeError
        '''
        if not type(novo_telefone) == int:
            raise TypeError('Telefone deve ser um número')
        self._tel = novo_telefone

    def get_email(self) -> str:
        '''
        Acessor do atributo Email
        '''
        return self._email

    def set_email(self, novo_email: str) -> None:
        '''
        Mutador do atributo Email, caso não receba um email válido
        retorna um ValueError
        '''
        if '@' not in novo_email:
            raise ValueError('Não é um email válido')
        self._email = novo_email


class Banco():
    """
    A classe Banco deverá receber um nome em sua construção e deverá
    implementar os métodos:
    abre_contas(clientes e saldo inicial): abre uma nova conta
    e lista_contas(): apresenta um resumo de todas as contas do banco
    DICA: mantenha uma variável interna qe armazene todas as contas do banco
    DICA2: utilze a variável acima para gerar automaticamente o número das
    contas do banco
    """
    def __init__(self, nome: str) -> None:
        self._nome = nome
        self._contas = []

    def get_nome(self) -> str:
        '''
        Acessor do Atributo Nome
        '''
        return self._nome

    def deposito_geral(self, valor):
        for conta in self._contas:
            conta.deposito(valor)

    def abre_conta_corrente(self, clientes: List[Cliente],
                            saldo_inicial: Number,
                            juros: float,
                            limite: Number) -> None:
        '''
        Método para abertura de nova conta, recebe os clientes
        o saldo inicial e a taxa de manutenção, caso o saldo inicial
        seja menor que 0 devolve um ValueError
        '''
        if saldo_inicial < 0:
            raise ValueError('O saldo inicial não pode ser negativo')
        c = ContaCorrente(clientes, len(self._contas) + 1,
                          saldo_inicial, juros, limite)
        self._contas.append(c)

    def abre_conta_poupanca(self, clientes: List[Cliente],
                            saldo_inicial: Number, juros: Number) -> None:
        '''
        Método para abertura de nova conta, recebe os clientes
        o saldo inicial e a taxa de manutenção, caso o saldo inicial
        seja menor que 0 devolve um ValueError
        '''
        if saldo_inicial < 0:
            raise ValueError('O saldo inicial não pode ser negativo')
        c = ContaPoupanca(clientes, len(self._contas) + 1,
                          saldo_inicial, juros)
        self._contas.append(c)

    def lista_contas(self) -> List['Conta']:
        '''
        Retorna a lista com todas as contas do banco
        '''
        return self._contas


class Conta():
    """
    Classe Conta base para outras contas.
    """
    def __init__(self, clientes: List[Cliente], numero_conta: int,
                 saldo_inicial: Number):
        self._clientes = clientes
        self._numero = numero_conta
        self._saldo = saldo_inicial
        self._op = [{'saldo inicial': saldo_inicial}]

    def get_clientes(self) -> List[Cliente]:
        '''
        Acessor para o atributo Clientes
        '''
        return self._clientes

    def get_saldo(self) -> Number:
        '''
        Acessor para o Atributo Saldo
        '''
        return self._saldo

    def set_saldo(self, novo_saldo: Number) -> None:
        '''
        Mutador para o atributo Saldo
        '''
        self._saldo = novo_saldo

    def get_numero(self) -> int:
        '''
        Acessor para o atributo Numero
        '''
        return self._numero

    def saque(self, valor: Number) -> None:
        '''
        Método de saque da classe Conta, operação deve aparecer no extrato
        '''
        self._saldo -= valor
        self.inclui_operacao_extrato({'saque': valor})

    def deposito(self, valor: Number):
        '''
        Método depósito da classe Conta, operação deve aparecer no extrato
        '''
        self._saldo += valor
        self.inclui_operacao_extrato({'deposito': valor})

    def inclui_operacao_extrato(self, operacao: Dict[str, Number]):
        '''
        Inclui operação na lista de operações da conta.
        Uma operação é um dicionário onde a chave éum string com o nome
        da operação, e o valor e o valor da operação.
        ex: {'saque':100}, {'deposito': 250.10}
        '''
        self._op.append(operacao)

    def extrato(self) -> List[Dict[str, Number]]:
        '''
        Retorna uma lista com as operações executadas na Conta
        '''
        return self._op


class ContaPoupanca(Conta):
    '''
    Classe Conta Poupança
    '''
    def __init__(self, clientes: List[Cliente], numero: int,
                 saldo_inicial: Number, juros: Number) -> None:
        super().__init__(clientes, numero, saldo_inicial)
        self._juros = juros

    def rendimentos(self) -> None:
        '''
        Calcula e adiciona no saldo da conta o valor dos rendimentos
        com base no saldo e na taxa de juros. esta operação de aparecer
        no extrato: {'rendimentos': valor}
        '''
        rend = self.get_saldo() * self._juros
        self.set_saldo(self.get_saldo() + rend)
        self.inclui_operacao_extrato({'rendimentos': rend})

    def saque(self, valor: Number) -> None:
        '''
        Saca o valor da conta, caso o valor a ser sacado seja
        maior que o saldo da conta, devolve um ValueError
        Esta operação deve aparecer no extrato.
        '''
        if valor > self.get_saldo():
            raise ValueError
        super().saque(valor)


class ContaCorrente(Conta):
    '''
    Classe Conta Corrente
    '''
    def __init__(self, clientes: List[Cliente], numero: int,
                 saldo_inicial: Number, juros: Number, limite: Number) -> None:
        super().__init__(clientes, numero, saldo_inicial)
        self._juros = juros
        self._limite = limite

    def cobra_juros(self) -> None:
        '''
        Cobra a taxa de juros da conta caso esteja dentro do cheque especial,
        esta operacao deve aparecer no extrato: {'juros': valor}
        '''
        if self.get_saldo < 0:
            j = self.get_saldo() * self._juros
            self.set_saldo(self.get_saldo() + j)
            self.inclui_operacao_extrato({'juros': abs(j)})

    def saque(self, valor: Number) -> None:
        '''
        Saca o valor da conta corrente, caso esteja dentro do saldo e do limite
        do cheque especial, caso contrário devolve um ValueError
        esta operação deve entrar no extrato
        '''
        if valor > self.get_saldo() + self._limite:
            raise ValueError
        super().saque(valor)
