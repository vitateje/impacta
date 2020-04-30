# Criar um dicionário
meu_dict = {'chave1':'valor1', 'chave2':'valor2'}
# Acessar um item do dicionário
meu_dict['chave1']
# colocar um novo item em um dicionário
meu_dict['nova_chave'] = 'valor'
# modificar um item de um dicionário
meu_dict['chave1'] = 'novo_valor'
# remover um item de um dicionário
del(meu_dict['chave1'])
# verificar se uma chave está no dicionário
'chave' in meu_dict
# possibilidades de chaves e valores
lista_contatos = {'joão': {'nome': 'João', 'email': 'joao@mail.com', 'cel': [9999999, 77777777]},
                  'maria': {'nome': 'Maria', 'email': 'maria@mail.com', 'cel': 8888888},
                  'jose': {'nome': 'Jose', 'email': 'jose@mail.com'}}
# iterar sobre um dicionário
for contato in lista_contatos:
    if 'cel' in lista_contatos[contato]:
        print(lista_contatos[contato]['nome'], lista_contatos[contato]['cel'])

print(lista_contatos['joão']['cel'][0])
# Exercício pré AC1
dic = {1:'um', 2:'dois'}
print(dic[2])