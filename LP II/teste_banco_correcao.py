from banco import Banco, Cliente

cl = Cliente('Fulano', 99999999, 'fulano@mail.com')
banco_legal = Banco('Banco Legal')

banco_legal.abre_conta_corrente([cl], 200, 0.1, 200)
banco_legal.abre_conta_poupanca([cl], 1000, 0.05)

banco_legal.deposito_geral(500)

for conta in banco_legal.lista_contas():
    print(conta.get_saldo())
