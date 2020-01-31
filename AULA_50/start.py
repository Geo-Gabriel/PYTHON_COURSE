'''
Criar uma nova pasta com o nome AULA50 dentro dela criar um novo virtualenv
$> where python
para achar o endereço python

criar uma aplicação flask que tenha os 4 metodos HTTP, quando chamados retorne uma string a classe controller e a rota dece ser 'pessoa'.
'''

from flask import  Flask
from flask_restful import Api
from AULA_50.controller.pessoa_controller import PessoaController

app = Flask(__name__)

api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')

@app.route('/')
def index ():
    return 'Testando API REST'

if __name__ == '__main__':
    app.run(debug=True, port=80)
