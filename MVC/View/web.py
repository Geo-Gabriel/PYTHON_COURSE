from flask import Flask, render_template
import sys
sys.path.append('/Users/900139/Desktop/GIT/PYTHON_COURSE/MVC')
from Controller.pessoa_controller import PessoaController

app = Flask(__name__)
pessoa_controller = PessoaController()
nome = 'Cadastros'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    pessoas = pessoa_controller.listar_todos()
    return render_template('listar.html', titulo_app = nome, lista = pessoas)

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html', titulo_app = nome)

app.run(debug=True)
