'''
Criar uma nova pasta com o nome AULA41 dentro dela criar um novo virtualenv
$> where python
para achar o endereço python

criar uma aplicação flask que tenha os 4 metodos HTTP, quando chamados retorne uma string a classe controller e a rota dece ser 'pessoa'.
'''

from flask import  Flask, render_template
from flask_restful import  Api
from AULA_41.venv_aula_41.controller.pessoa_controller import PessoaController
p_c = PessoaController()

app = Flask(__name__)

api = Api(app)

api.add_resource(PessoaController, f'/api/cep')

@app.route('/')
def index ():
    return p_c.get()

if __name__ == '__main__':
    app.run(debug=True, port=80)
