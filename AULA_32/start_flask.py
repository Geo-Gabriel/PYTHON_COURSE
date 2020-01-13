# INTEGRANDO BANCO DE DADOS MYSQL COM FLASK

import MySQLdb
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def voltar ():
    return render_template('index.html')

app.run(debug=True)