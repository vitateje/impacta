from flask import Blueprint, request, jsonify
from to_dict import *
from validacao import *
from migration import conectar, create_database
from contextlib import closing

import sqlite3

disciplina = Blueprint("disciplina", __name__)

@disciplina.route("/disciplinas", methods = ["GET"])
def disciplina_retorna_lista():
    sql = """SELECT * FROM disciplina"""
    resultados = []
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql)
        linhas = cursor.fetchall()
        for id, nome, plano_ensino, carga_horaria, status, id_coordenador in linhas:
            resultados.append({"id": id, "nome": nome, "plano_ensino": plano_ensino,
                "carga_horaria": carga_horaria, "status": status, "id_coordenador": id_coordenador})
        return jsonify(resultados), 200

@disciplina.route('/disciplinas/<int:id>', methods = ["GET"])
def disciplina_por_id(id):
    sql = "SELECT id, nome, id_coordenador, carga_horaria, plano_ensino, status FROM disciplina WHERE id = ?"
    resultados = []
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (id,))
        r = cursor.fetchall()
        if r == None: return None
        for carga_horaria, id, id_coordenador, nome, plano_ensino, status  in r:
            resultados.append({"id": id, "nome": nome, "plano_ensino": plano_ensino,
                "carga_horaria": carga_horaria, "status": status, "id_coordenador": id_coordenador})
        return jsonify(resultados), 200

@disciplina.route("/disciplinas", methods = ["POST"])
def adiciona_disciplinas():
    dados = request.get_json()
    params = (dados['nome'],dados['plano_ensino'],dados['carga_horaria'],dados['status'],dados['id_coordenador'],)
    sql = """INSERT INTO disciplina (nome, plano_ensino, carga_horaria, status, id_coordenador)
                VALUES (?,?,?,?,?)"""
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(cursor.lastrowid)
  
@disciplina.route("/disciplinas/<int:id>", methods = ["PUT"])
def editar_disciplina(id):
    dados = request.get_json()
    params = (dados['nome'], id)
    sql = "UPDATE disciplina SET nome = ? WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(dados['nome']), 200

@disciplina.route("/disciplinas/<int:id>", methods = ["DELETE"])
def deletar_disciplina(id):
    params = (id,)
    sql = "DELETE FROM disciplina WHERE id = ?"
    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(sql, (params))
        conn.commit()
        return jsonify(id), 200
