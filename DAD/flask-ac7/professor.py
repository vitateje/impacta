from flask import Blueprint, request, jsonify
from to_dict import *
from validacao import *
from migration import conectar, create_database
from contextlib import closing

professor = Blueprint("professor", __name__)

#professores
@professor.route("/professores", methods = ["GET"])
def professores_retorna_lista():
    sql = """SELECT * FROM professor"""
    resultados = []
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for id, nome in linhas:
            resultados.append({"id": id, "nome": nome})
        return jsonify(resultados), 200

@professor.route('/professores/<int:id>', methods = ["GET"])
def professor_por_id(id):
    sql = "SELECT id, nome FROM professor WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (id, ))
        r = cursor.fetchone()
        if r == None: return None
        return {"id": r[0], "nome": r[1]}

@professor.route("/professores", methods = ["POST"])
def adiciona_professores():
    dados = request.get_json()
    params = (dados['nome'],)
    sql = "INSERT INTO professor (nome) VALUES (?)"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(cursor.lastrowid)
  

@professor.route("/professores/<int:id>", methods = ["PUT"])
def editar_professor(id):
    dados = request.get_json()
    params = (dados['nome'], id)
    sql = "UPDATE professor SET nome = ? WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(dados['nome']), 200


@professor.route("/professores/<int:id>", methods = ["DELETE"])
def deletar_professor(id):
    params = (id,)
    sql = "DELETE FROM professor WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(id), 200
