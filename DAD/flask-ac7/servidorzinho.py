from flask import Flask, jsonify
from contextlib import closing
from migration import conectar, create_database

import sqlite3

app = Flask(__name__)

create_database()

from aluno import aluno as aluno_blueprint
app.register_blueprint(aluno_blueprint)

from professor import professor as professor_blueprint
app.register_blueprint(professor_blueprint)

from disciplina import disciplina as disciplina_blueprint
app.register_blueprint(disciplina_blueprint)

if __name__ == "__main__":
    app.run(port = 5002)
