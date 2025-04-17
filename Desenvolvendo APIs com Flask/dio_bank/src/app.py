from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'hi, World!'  


@app.route('/bem vindo')
def hello_world():
    return '<h1>Bem Vindo!</h1>'  