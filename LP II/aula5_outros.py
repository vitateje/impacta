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

# by myself: 

joao = {'nome':'Joao', 'email':'vita@gmail.com', 'cel':988887777}
maria = {'nome':'Maria', 'email':'mara@gmail.com', 'cel':988887777}
jose = {'nome':'Jose', 'email':'vita@gmail.com'}

#print(joao,maria,jose)

lista_contatos = [{'nome':'Joao', 'email':'vita@gmail.com', 'cel':988887777},{'nome':'Maria', 'email':'mara@gmail.com', 'cel':988887777},
{'nome':'Jose', 'email':'vita@gmail.com'}]

lista_contatos = {'joao':{'nome':'Joao', 'email':'vita@gmail.com', 'cel':988887777},
'maria': {'nome':'Maria', 'email':'mara@gmail.com', 'cel':988887777},
'jose': {'nome':'Jose', 'email':'vita@gmail.com'}

print(lista_contatos)

#chave int or str

