from flask import Flask, render_template
import sys
sys.path.append('')
from AULA_41.controller.pessoa_controller import PessoaController

app = Flask(__name__)

pessoa_c = PessoaController()

@app.route('/')

def start():
    pessoas = pessoa_c.listar_todos()
    return render_template('index.html', lista=pessoas)

app.run()
