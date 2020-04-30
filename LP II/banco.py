__alunos__ = ["vitor.teixeira@aluno.faculdadeimpacta.com.br",
              "gabriel.neves@aluno.faculdadeimpacta.com.br"]


class Cliente():
    def __init__(self, nome_cliente, telefone_cliente, email_cliente):
        self._nome = nome_cliente
        self._telefone = telefone_cliente
        self._email = email_cliente

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        pass

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, telefone):
        if type != int:
            print('Nao é numero')

    def get_email(self):
        return self._email

    def set_email(self, email):
        if email == '%@%':
            return email


class Banco():
    def __init__(self, nome, contas):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abre_conta(self, clientes, saldo_inicial):
        self.contas.append(self.contas)

    def lista_contas(self):
        for c in self.contas:
            c.resumo()


class Conta():
    def __init__(self, lista_clientes, numero_conta, saldo_inicial):
        self.lista_clientes = lista_clientes
        self.numero = numero_conta
        self.saldo = saldo_inicial
        self.operacoes = []
        self.operacoes.append({'Inicial': saldo_inicial})

    # def add_cliente(self):
    # self.lista_clientes.append([lista_clientes])

    def saque(self, valor):
        self.saldo -= valor
        self.operacoes.append(['Saque', valor, 'Saldo', self.saldo])

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(['Deposito', valor, 'Saldo', self.saldo])

    def extrato(self):
        print('Extrato CC Nº', self.numero, self.operacoes)
