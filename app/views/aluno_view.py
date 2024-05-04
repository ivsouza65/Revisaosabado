from app import app
from flask import render_template

@app.route("/cadaluno")
def cadastrar_aluno():
    return render_template("aluno/cad_aluno.html")