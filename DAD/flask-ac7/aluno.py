from flask import Blueprint, request, jsonify
from to_dict import *
from validacao import *
import sqlite3
from migration import conectar, create_database
from contextlib import closing

aluno = Blueprint("aluno", __name__)

@aluno.route("/hello")
def hello():
    return "Hello, aluno"

@aluno.route("/reseta", methods = ["POST"])
def reseta():
    sqlaluno = """DELETE FROM aluno"""
    sqldisciplina = """DELETE FROM disciplina"""
    sqlprofessor = """DELETE FROM professor"""
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sqlaluno)
        cursor.execute(sqldisciplina)
        cursor.execute(sqlprofessor)
        conn.commit()
        return jsonify({'sucess': 'reset efetuado com suceso'}), 200

@aluno.route("/alunos", methods = ["GET"])
def alunos_retorna_lista():
    sql = """SELECT * FROM aluno"""
    resultados = []
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for id, nome in linhas:
            resultados.append({"id": id, "nome": nome})
        return jsonify(resultados), 200
    #return jsonify(alunos), 200

@aluno.route('/alunos/<int:id>', methods = ["GET"])
def aluno_por_id(id):
    sql = "SELECT id, nome FROM aluno WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (id, ))
        r = cursor.fetchone()
        if r == None: return None
        return {"id": r[0], "nome": r[1]}


@aluno.route("/alunos", methods = ["POST"])
def adiciona_alunos():
    dados = request.get_json()
    params = (dados['nome'],)
    sql = "INSERT INTO aluno (nome) VALUES (?)"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(cursor.lastrowid)
  


@aluno.route("/alunos/<int:id>", methods = ["PUT"])
def editar_aluno(id):
    dados = request.get_json()
    params = (dados['nome'], id)
    sql = "UPDATE aluno SET nome = ? WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(dados['nome']), 200

#    for aluno in alunos:
#        if aluno['id'] == id:
#            aluno['nome'] = request.get_json().get('nome')
#            return jsonify(aluno), 200
#    return jsonify({'erro': 'aluno não encontrado'}), 404

@aluno.route("/alunos/<int:id>", methods = ["DELETE"])
def deletar_aluno(id):
    params = (id,)
    sql = "DELETE FROM aluno WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(id), 200