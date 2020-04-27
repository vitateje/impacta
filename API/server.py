# SERVER #

# modo servidor // servindo infos by APIs **

from flask import Flask, jsonify, request
from requests import api

app = Flask(__name__)

#base = {'id':1, 'nome':'Vitor'}
base = [{'id':1, 'nome':'Vitor'}]
#base = {'Usuario': ['Vitor','Bruno','Vinicius'], 'Codigo': 'Lucas'}
#base = {'Title': ['Vitor','Bruno','Vinicius'], 2: 'Lucas'}
#base = ['id':1, 'nome':'Vitor']

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/teste')
def consulta_all():
    #  base = {1 : 'vitor'}
    dic = jsonify(base)  # o jsonify renderiza no template um DIC ( pode ser usado para consumo ) # dessa maneira estou servindo informações.
    return dic


@app.route('/teste', methods=['POST'])
def adiciona():
    #novo_aluno = request.json
    dados = request.get_json()
    #base['Usuario'].append(dados)
    base.append(dados)
    #return jsonify(base['Usuario'])
    return jsonify(base)


@app.route('/teste/<int:id>', methods=['PUT'])
def atualiza(id):
    dados = request.get_json()
    for x in base:
        if x['id'] == id:
            x['nome'] = dados.get('nome')
    return jsonify(base)


@app.route('/teste/<int:id>', methods=['DELETE'])
def deleta(id):
    dados = request.get_json()
    for x in range(0, len(base)):
        if base[x]['id'] == id:
            del(base[x]['nome'])
            return jsonify(base)

    # for i in range(0, len(base)):
    #     if base[i]['id'] == id:
    #         del base[i]
    #         return jsonify({'message': 'aluno removido com suceso'}), 200
    # return jsonify({'erro': 'professor nao encontrado'}), 400


if __name__ == "__main__":
    app.run(port=5002)
