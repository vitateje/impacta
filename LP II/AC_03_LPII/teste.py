from clientes import Cliente
from contas import Conta
from bancos import Banco

joao = Cliente('Jhonny Bravo', '8899-9999')
maria = Cliente('Maria da Silva', '9999-0000')

conta1 = Conta('joao', 1, 1000)
conta2 = Conta('maria', 2, 500)

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta1.saque(250)
conta1.extrato()
conta2.extrato()
