class Conta(object):
    def __init__(self, saldo):
        self.saldo = saldo

    def __len__(self):
        return abs(self.saldo)

    def __str__(self):
        return f'Conta:\nsaldo: {self.saldo}'

#cc = Conta(150)
#cc2 = Conta(-350)

#print('olar')
#print([1,2,3])
#print(cc)
#print(cc2)


def chama_pessoa(nome: str,  sobrenome, apelido: str = None, idade = None):
    if apelido:
        print(f'Ow, {apelido}!')
    else:
        print(f'Ow, {nome} {sobrenome}!')
    if idade:
        print(f'vc tem {idade} anos mesmo?')


chama_pessoa( 'de tal', 'Fulano', False, 20)