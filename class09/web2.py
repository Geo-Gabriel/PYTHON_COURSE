# AULA 09 -- 19-11-2019
# WEB 02

from flask import Flask

app = Flask(__name__)

@app.route('/')
def incia():
    return '''  '''
app.run()