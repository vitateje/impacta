from contextlib import closing

import sqlite3

def conectar():
    return sqlite3.connect("escola.db")

def create_database():
    disciplina = ("""
    CREATE TABLE IF NOT EXISTS disciplina (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL,
        plano_ensino VARCHAR(254) NOT NULL,
        carga_horaria INT NOT NULL,
        status INT NOT NULL,
        id_coordenador INT
    )""")

    professor = ("""
    CREATE TABLE IF NOT EXISTS professor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL
    )""")

    aluno = ("""
    CREATE TABLE IF NOT EXISTS aluno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50) NOT NULL
    )""")

    with closing(conectar()) as conn, closing(conn.cursor()) as cursor:
        cursor.execute(disciplina)
        cursor.execute(aluno)
        cursor.execute(professor)
        conn.commit()