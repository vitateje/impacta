dic = {
    "integrantes": {
        "beatles":['ringo','john','paul','george','pete'],
        "the_fellowship_of_the_ring":['gandolfo','aragorn','gimli','legolas','boromir','frodo','sam','hobbit 3','hobbit 4'],
        "The_Vindicators":  ('Vance Maximus', 'Alan Rails', 'Crocubot',
                             'Million Ants', 'Morty Smith', 'Rick Sanchez', 'Lady Katana', 'Calypso', 'Diablo Verde'),
        'Alunos_distraidos_nesse_momento': [],
        },
    "jogos" : [
         {"nome":"CS go", "empresa":"valve", "estilo": "FPS"},
         {"nome":"PLANESCAPE:torment", "empresa":"Bioware", "estilo": "Jogo mais bem escrito da história"},
         {"nome":"The Witcher", "empresa":"CD Project Red", "estilo": "Open World RPG"},
        ],
    }

print(dic["jogos"][2]["nome"] == "The Witcher")
print("CS go" == dic["jogos"][0])
print("FPS" in dic["jogos"]["CS go"])
print("Rick Sanchez" in dic.integrantes.The_vindicators)
print(dic["integrantes"]["beatles"][3] == "paul")
print("valve" in dic["jogos"]["CS go"])
print("empresa" in dic["jogos"]["CS go"])
print("legolas" in dic["integrantes"]["the_fellowship_of_the_ring"])
print("merlin" in dic["integrantes"]["The_Vindicators"])
print("Thor" in dic["filmes"]["Avengers"])
print("Open World RPG" == dic["jogos"][1]["empresa"])
print(dic["jogos"][0]["estilo"] == "FPS")
print(dic["jogos"]["Bioware"] == "PLANESCAPE:torment")
print("pete" in dic["integrantes"]["beatles"])
print(dic["integrantes"]["the_fellowship_of_the_ring"][2] == "gimli")
print("CD Project RED" in dic["jogos"][2])
print("empresa" in dic["jogos"][2])
print(dic[dic] + dic[dic[dic]])
