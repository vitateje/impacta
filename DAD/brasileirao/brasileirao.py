'''
Nessa atividade, vamos usar dados do campeonato brasileiro 2018
(brasileirão) para estudar como acessar listas, dicionários,
e estruturas encadeadas (listas dentro de dicionários dentro de listas).

Os dados estão fornecidos em um arquivo (ano2018.json) que você 
pode abrir no firefox, para tentar entender melhor.

Se quiser ver os dados dentro do python, pode chamar a função
pega_dados.
'''

'''
1. Crie uma função datas_de_jogo, que procura nos dados do brasileirão
recebidas no parâmetro e devolve uma lista de todas as datas em que houve jogo.

As datas devem ter o mesmo formato que tinham nos dados do brasileirão.

Dica: busque em dados['fases'].

Observe que essa função (e todas as demais) recebem os dados dos
jogos num parâmetro chamado "dados". Essa variável contém todas as
informações que foram lidas do arquivo JSON que acompanha essa atividade.
'''


def datas_de_jogo(dados):
    lista = []
    for x in dados['fases']['2700']['jogos']['data']:
        lista.append(x)
    return lista


'''
2. Crie uma função data_de_um_jogo, que recebe a id numérica de um jogo
e devolve a data em que ele ocorreu.

Se essa nao é uma id válida, você deve devolver a string 'não encontrado'.
Cuidado! Se você devolver uma string ligeiramente diferente, o teste
vai falhar.

(você provavelmente vai querer testar sua função no braço e não
somente fazer os meus testes. Para isso, note que muitos números
nesse arquivo estão representados não como números, mas como strings)
'''


def data_de_um_jogo(dados, id_jogo):
    if id_jogo not in dados['fases']['2700']['jogos']['id']:
        return f'não encontrado'
    return dados['fases']['2700']['jogos']['id'][id_jogo]['data']


'''
3. Nos nossos dados, cada time tem um id, uma identificação numérica.
(você pode consultar as identificações numéricas em dados['equipes']).

Essas ids também aparecem nos jogos (onde? dê uma procurada!)

A próxima função recebe a id numérica de um jogo, e devolve as
ids numéricas dos dois times envolvidos.

Vou deixar um código pra você lembrar como retornar duas ids em
um único return.

def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = 12
    time2 = 13
    return time1, time2 # Assim, retornamos as duas respostas em um único return.
'''


def ids_dos_times_de_um_jogo(dados, id_jogo):
    time1 = dados['fases']['2700']['jogos']['id'][id_jogo]['time1']
    time2 = dados['fases']['2700']['jogos']['id'][id_jogo]['time2']
    return time1, time2  # Assim, retornamos as duas respostas em um único return.


'''
4. A próxima função recebe a id_numerica de um time e deve retornar o seu 'nome-comum'.
'''


def nome_do_time(dados, id_time):
    return dados['equipes'][id_time]['nome-comum']


'''
5. A próxima função "cruza" as duas anteriores. Recebe uma id de um jogo
e retorna os "nome-comum" dos dois times.
'''


def nomes_dos_times_de_um_jogo(dados, id_jogo):
    id_time = ids_dos_times_de_um_jogo(dados, id_jogo)
    t1 = nome_do_time(dados, id_time[0])
    t2 = nome_do_time(dados, id_time[1])
    return t1, t2


'''
6. Façamos agora a busca "ao contrário". Conhecendo
o nome-comum de um time, queremos saber a sua id.

Se o nome comum não existir, retorne 'não encontrado'.
'''


def id_do_time(dados, nome_time):
    lista = []
    for x in dados['equipes']:
        if nome_time == dados['equipes'][x]['nome-comum']:
            return dados['equipes'][x]['id']
    return f'não encontrado'


'''
7. Agora, façamos uma busca "fuzzy". Queremos procurar por 'Fla'
e achar o Flamengo. Ou por 'Paulo' e achar o São Paulo.

Nessa busca, você recebe um nome, e verifica os campos
'nome-comum', 'nome-slug', 'sigla' e 'nome',
tomando o cuidado de aceitar times se a string
buscada aparece dentro do nome (A string "Paulo"
aparece dentro de "São Paulo").

Sua resposta deve ser uma lista de ids de times que "batem"
com a pesquisa (e pode ser vazia, se não achar ninguém).
'''


def busca_imprecisa_por_nome_de_time(dados, nome_time):
    lista = []
    for x in dados['equipes']:
        if nome_time in dados['equipes'][x]['nome-comum'] or nome_time in dados['equipes'][x]['nome-slug'] or nome_time in dados['equipes'][x]['nome'] or nome_time in dados['equipes'][x]['sigla']:
            lista.append(dados['equipes'][x]['id'])
    return lista


'''
8. Agora, a ideia é receber a id de um time e retornar as
ids de todos os jogos em que ele participou.
'''


def ids_de_jogos_de_um_time(dados, time_id):
    lista = []
    for x in dados['fases']['2700']['jogos']['id']:
        if time_id == dados['fases']['2700']['jogos']['id'][x]['time1'] or time_id == dados['fases']['2700']['jogos']['id'][x]['time2']:
            lista.append(x)
    return lista


'''
9. Usando as ids dos jogos em que um time participou, podemos descobrir
em que dias ele jogou.

Note que essa função recebe o nome-comum do time, não a sua id.

Ela retorna uma lista das datas em que o time jogou.
'''


def datas_de_jogos_de_um_time(dados, nome_time):
    datas = []
    id_time = id_do_time(dados, nome_time)
    id_jogos = ids_de_jogos_de_um_time(dados, id_time)
    for x in id_jogos:
        datas.append(data_de_um_jogo(dados, x))
    return datas


'''
10. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve um dicionário, com quantos gols cada time fez.
'''


def dicionario_de_gols(dados):
    dic = {}
    for x in dados['equipes']:
        idtime = x
        lista_jogos = ids_de_jogos_de_um_time(dados, x)
        for a in lista_jogos:
            if idtime == dados['fases']['2700']['jogos']['id'][a]['time1']:
                if idtime in dic:
                    dic[idtime] += int(dados['fases']['2700']['jogos']['id'][a]['placar1'])
                else:
                    dic[idtime] = int(dados['fases']['2700']['jogos']['id'][a]['placar1'])
            elif idtime == dados['fases']['2700']['jogos']['id'][a]['time2']:
                if idtime in dic:
                    dic[idtime] += int(dados['fases']['2700']['jogos']['id'][a]['placar2'])
                else:
                    dic[idtime] = int(dados['fases']['2700']['jogos']['id'][a]['placar2'])
    return dic


'''
11. A próxima função recebe apenas o dicionário dos dados do brasileirão.

Ela devolve a id do time que fez mais gols no campeonato.
'''


def time_que_fez_mais_gols(dados):
    timegoleador = 0
    for k, v in dicionario_de_gols(dados).items():
        if v > timegoleador:
            timegoleador = v
            idtime = k
    return idtime


'''
12. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela devolve um dicionário. Esse dicionário conta, para cada estádio,
quantas vezes ocorreu um jogo nele.

Ou seja, as chaves são ids de estádios e os valores associados,
o número de vezes que um jogo ocorreu no estádio.
'''


def dicionario_id_estadio_e_nro_jogos(dados):
    dic = {}
    for x in dados['fases']['2700']['jogos']['id']:
        idestadio = dados['fases']['2700']['jogos']['id'][x]['estadio_id']
        if idestadio in dic:
            dic[idestadio] += 1
        else:
            dic[idestadio] = 1
    return dic


'''
13. A próxima função recebe apenas o dicionário dos dados do brasileirão

Ela retorna o número de times que o brasileirão qualifica para a libertadores.
Ou seja, devolve quantos times são classificados para a libertadores (consultando
o dicionário de faixas).

Note que esse número está nos dados recebidos no parâmetro e você deve pegar esse
número daí. Não basta retornar o valor correto, tem que acessar os dados
fornecidos.
'''


def qtos_libertadores(dados):
    classifica = dados['fases']['2700']['faixas-classificacao']['classifica1']
    listaclassifica = []
    for x in classifica['faixa']:
        listaclassifica.append(x)
    listaliberta = []
    dic = dados['fases']['2700']['classificacao']['grupo']['Único']
    for index, item in enumerate(dic):
        if index >= int(listaclassifica[0]) and index <= int(listaclassifica[2]):
            listaliberta.append(index)
    return(len(listaliberta))


'''
14. A próxima função recebe um tamanho, e retorna uma lista
com len(lista) = tamanho, contendo as ids dos times melhor classificados.
'''


def ids_dos_melhor_classificados(dados, numero):
    dic = dados['fases']['2700']['classificacao']['grupo']['Único']
    lista = []
    numero = numero-1
    for index, item in enumerate(dic):
        if index <= numero:
            lista.append(item)
    return lista


'''
15. A próxima função usa as duas anteriores para retornar uma 
lista de todos os times classificados para a libertadores em
virtude do campeonato brasileiro.

Lembre-se de consultar a estrutura, tanto para obter a classificação, quanto
para obter o número correto de times a retornar.

A função só recebe os dados do brasileirão.
'''


def classificados_libertadores(dados):
    numero = qtos_libertadores(dados)
    return ids_dos_melhor_classificados(dados, numero)


'''
16. Da mesma forma que podemos obter a informação dos times classificados
para a libertadores, também podemos obter os times na zona de rebaixamento.

A próxima função recebe apenas o dicionário de dados do brasileirão,
e retorna uma lista com as ids dos times rebaixados.

Consulte a zona de rebaixamento do dicionário de dados, não deixe
ela chumbada da função.
'''


def rebaixados(dados):
    classifica = dados['fases']['2700']['faixas-classificacao']['classifica3']
    listaclassifica = []
    for x in classifica['faixa']:
        listaclassifica.append(x)
    listaliberta = []
    intervalo1 = listaclassifica[0] + listaclassifica[1]
    intervalo1n = int(intervalo1)-1
    intervalo2 = listaclassifica[3] + listaclassifica[4]
    intervalo2n = int(intervalo2)-1
    dic = dados['fases']['2700']['classificacao']['grupo']['Único']
    for index, item in enumerate(dic):
        if index >= intervalo1n and index <= intervalo2n:
            listaliberta.append(item)
    return listaliberta


'''
17. A próxima função recebe (além do dicionario de dados do brasileirão) uma id de time.

Ela retorna a classificação desse time no campeonato.

Se a id nao for válida, ela retorna a string 'não encontrado'.
'''


def classificacao_do_time_por_id(dados, time_id):
    classifica = dados['fases']['2700']['classificacao']['grupo']['Único']
    for classificacao, idtime in enumerate(classifica):
        if time_id == idtime:
            return classificacao+1
    return f'não encontrado'
