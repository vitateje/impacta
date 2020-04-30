''' Criar um dicionario - estrutura de dados nao ordenadas
 - chave/valor - identificador unico '''

meu_dict = {'manga':3, 'maca':12, 'limao': 'nao comprar' }
print(meu_dict)
meu_dict['manga']


# Acessar um item do dicionario
meu_dict['manga']

#colocar um novo item no dict
meu_dict['pera']=5
print(meu_dict)

#modificar um item
meu_dict['chave'] = 'novo_valor'
meu_dict['maca']=6
print(meu_dict)

#remover um item
del(meu_dict['limao'])
print(meu_dict)

'limao' in meu_dict 

#possibilidades de chaves e valores