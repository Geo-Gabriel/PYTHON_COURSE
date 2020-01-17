from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def start():
    return render_template('index.html', titulo_app = 'Cadastros')

@app.route('/listar')

def listar():
    return render_template('listar.html', titulo_app='Listar')

@app.route('/cadastrar')

def cadastrar ():
    return render_template('/cadastrar.html', titulo_app='Cadastrar')

app.run(debug=True)

def vazio (dado):
    if dado:
        return dado
    else:
        return ''
    
print(vazio(rua))

# -- If ternário em python

print(rua if rua else '')

