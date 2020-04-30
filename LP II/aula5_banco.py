class Banco():
    def __init__(self, numero_banco, numero_agencia, numero_conta):
        self.banco = numero_banco
        self.agencia = numero_agencia
        self.conta = numero_conta
        self.saldo = 0
        

    def saldo_conta(self):
        self.saldo = 0
        valor_saque = float(input('digite o valor do saque:'))
        self.saldo +=  #rever logica
        

info_banco = Banco ( '001','8888','01003344')

print(info_banco.banco,info_banco.agencia,info_banco.conta)
info_banco.saldo_conta()
print('Saldo:',info_banco.saldo)
