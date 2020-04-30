from models import Guerreiro, Mago

def test_criacao_guerreiro():
    #Arrange
    #Act
    g = Guerreiro('Arthur', 100)
    
    #Assert
    assert g.nome == 'Arthur'
    assert g.vida == 100

def test_criacao_mago():
    #Arrange
    #Act
    m = Mago('Merlin', 60)
    
    #Assert
    assert m.nome == 'Merlin'
    assert m.vida == 60

def test_ataque_guerreiro_frente():
    #Arrange
    g = Guerreiro('Arthur', 100)

    #Act
    definicao_ataque = g.ataque('frente')

    #Assert
    assert definicao_ataque.potencia == 33
    assert definicao_ataque.distancia == 1
    assert definicao_ataque.direcao == 'frente'
