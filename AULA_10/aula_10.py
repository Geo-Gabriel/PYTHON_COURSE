# Aula 10 --- 20-11-2019
# Web 

name_page = 'Calculadora V1.0'

from flask import Flask, render_template, request
from calculos import *

app = Flask(__name__)

@app.route ('/')
def inicia():
    return render_template('index.html', titulo = name_page)

@app.route('/calcular')
def calculo ():
    a = int(request.args['a'])
    b = int(request.args['b'])
    r_soma = soma(a,b)
    r_subtracao = subtracao(a,b)
    r_produto = produto(a,b)
    r_divisao = divisao(a,b)
    r_divisaofracionada = divisao_fracionada(a,b)
    r_resto = resto_divisao(a,b)
    r_raiz = raiz_a_b(a,b)

    dicionario = {'soma': r_soma, 'subtracao': r_subtracao, 'produto': r_produto, 'divisao_int':r_divisao, 'divisao_frac':r_divisaofracionada, 'resto': r_resto, 'raiz': r_raiz}

    return render_template ('resultado.html'
    ,a = a
    ,b = b
    ,dicionario = dicionario)
    

app.run(debug=True)