

class Pokemon():
	def __init__(self, nome, hp, mp, turn):
        self.nome = nome
		self.hp = hp
		self.mp = mp
		self.turn = turn


	def atack(self, pokemon):
		self.turn = self.turn - 2
		pokemon 
		pass


Bulba = Pokemon('Bulba', 300, 400, 10)
print(f'O nome do pokemon é: {Bulba.nome} e seu HP é:{Bulba.hp}')
