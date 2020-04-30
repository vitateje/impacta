from flask import Flask, request, jsonify
from to_dict import *
from validacao import *

alunos = []
professores = []    

app = Flask(__name__)
app.register_blueprint(alunos_app)
app.register_blueprint(professores_app)

@app.route("/hello")
def hello():
    return "Hello, aluno"

@app.route("/reseta", methods = ["POST"])
def reseta():
    alunos.clear()
    professores.clear()
    return jsonify({'sucess': 'reset efetuado com suceso'}), 200

@app.route("/alunos", methods = ["GET"])
def alunos_retorna_lista():
    return jsonify(alunos), 200

@app.route('/alunos/<int:id>', methods = ["GET"])
def aluno_por_id(id):
    for aluno in alunos:
        if aluno['id'] == id:
            return jsonify(aluno), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400

@app.route("/alunos", methods = ["POST"])
def adiciona_alunos():
    dados = request.get_json()
    try:
        if "nome" in dados:
            validar_campos(dados, {'nome': str_nao_vazio, 'id': natural})
            for aluno in alunos:
                if aluno['id'] == dados['id']:
                    return jsonify({'erro': 'id ja utilizada'}), 400
            alunos.append(dados)
            return jsonify(to_dict(dados)), 200
        else:
            return jsonify({'erro': 'aluno sem nome'}), 400
    except:
        return jsonify({'erro': 'aluno nao encontrado'}), 400
  


@app.route("/alunos/<int:id>", methods = ["PUT"])
def editar_aluno(id):
    dados = request.get_json()
    if "nome" not in dados:
        return jsonify({'erro': 'aluno sem nome'}), 400
    for aluno in alunos:
        if aluno['id'] == id:
            aluno['nome'] = request.get_json().get('nome')
            return jsonify(aluno), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400

@app.route("/alunos/<int:id>", methods = ["DELETE"])
def deletar_aluno(id):
    for i in range(0, len(alunos)):
        if alunos[i]['id'] == id:
            del alunos[i]
            return jsonify({'message': 'aluno removido com suceso'}), 200
    return jsonify({'erro': 'aluno nao encontrado'}), 400

#professores
@app.route("/professores", methods = ["GET"])
def professores_retorna_lista():
    return jsonify(professores), 200

@app.route('/professores/<int:id>', methods = ["GET"])
def professor_por_id(id):
    for professor in professores:
        if professor['id'] == id:
            return jsonify(professor), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400

@app.route("/professores", methods = ["POST"])
def adiciona_professores():
    dados = request.get_json()
    if not "nome" in dados:
        return jsonify({'erro': 'professor sem nome'}), 400
    try:
        validar_campos(dados, {'nome': str_nao_vazio, 'id': natural})
        for professor in professores:
            if professor['id'] == dados['id']:
                return jsonify({'erro': 'id ja utilizada'}), 400
        professores.append(dados)
        return jsonify(to_dict(dados)), 200
    except:
        return jsonify({'erro': 'professor nao encontrado'}), 400
  

@app.route("/professores/<int:id>", methods = ["PUT"])
def editar_professor(id):
    dados = request.get_json()
    if not "nome" in dados:
        return jsonify({'erro': 'professor sem nome'}), 400
    for professor in professores:
        if professor['id'] == id:
            professor['nome'] = request.get_json().get('nome')
            return jsonify(professor), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400


@app.route("/professores/<int:id>", methods = ["DELETE"])
def deletar_professor(id):
    for i in range(0, len(professores)):
        if professores[i]['id'] == id:
            del professores[i]
            return jsonify({'message': 'aluno removido com suceso'}), 200
    return jsonify({'erro': 'professor nao encontrado'}), 400

if __name__ == "__main__":
    app.run(port = 5002)