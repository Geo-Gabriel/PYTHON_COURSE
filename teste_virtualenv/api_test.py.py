from flask import Flask
from flask_restful import Api
from controllers.cerveja_controller import  CervejaController

app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')

@app.route('/')
def inicio():
    return 'Welcome to API'

app.run(debug=True, port=80)
