from models import Personagem
import sys

classe_personagem = None

if len(sys.argv) > 1:
    classe_personagem = sys.argv[1]
else:
    classe_personagem = input('Escolha seu tipo de personagem: ')

pers = Personagem.cria_personagem(classe_personagem)
print(pers.ataque('frente'))