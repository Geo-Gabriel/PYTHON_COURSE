# aula 8  -- 18-11-2019
# WEB

from flask import Flask

app = Flask(__name__)

@app.route('/') # Qual rota quero que minha função responda -- A rota principal é '/' barra

def inicio():
    return 'Welcome to the real world my friends'

app.run()