''' Estudo do loop FOR e Dicionario '''

sl_faculdade = {'sala1': 'ADS A', 'sala2': 'SI A'}

print('Dicionario das Salas:', sl_faculdade)

for chave in sl_faculdade:  # membership
    print(sl_faculdade[chave])  # imprime os valores das chaves #

print(len(sl_faculdade))

lista = ['vitor', 'gabi', 'ale']
new_dict = {}


def add_dic():
    cont = 1
    # soma = 0
    for nome in lista:
        new_dict[cont] = nome
        cont += 1
    return new_dict


add_dic()

for x in new_dict:
    print(f'Os nomes são: {new_dict[x]}')
