from flask import Flask, jsonify, request

app = Flask(__name__)

database = {}
database['ALUNO'] = []
database['PROFESSOR'] = []

@app.route('/')
def all():
    return jsonify(database)

@app.route('/alunos')
def alunos():
    return jsonify(database['ALUNO'])

@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])

@app.route('/alunos', methods=['POST'])
def novo_aluno():
    novo_aluno = request.json
    database['ALUNO'].append(novo_aluno)
    return jsonify(database['ALUNO'])

@app.route('/alunos/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
     for aluno in database['ALUNO']:
         if aluno['id'] == id_aluno:
             return jsonify(aluno)
     return 'nao achei', 404

@app.route('/alunos/<int:id_aluno>', methods=['PUT'])
def atualizar(id_aluno):
    dados = request.get_json() # chamada para pegar as infos de um json
    index = 0
    for aluno in database['ALUNO']: # percorrendo banco de dados
        if aluno['id'] == id_aluno: # comparando parametros de URL x ID do banco
            aluno['id'] = dados['id'] # atribuindo infos do json para o do BD
            aluno['nome'] = dados['nome'] # atribuindo infos do json para o do BD
            return jsonify(aluno) # retorna todas as infos de Aluno em Json
        index += 1

@app.route('/alunos/<int:id_aluno>', methods=['DELETE'])
def remover(id_aluno):
    index = 0
    for aluno in database['ALUNO']:
        if aluno['id'] == id_aluno:
            del database['ALUNO'][aluno['id']]
            return jsonify(aluno)
        index += 1
    return '', 404

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)