import os

from flask import Flask
import db  # Importação absoluta em vez de relativa


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='diobank.sqlite',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    
    # Registra o módulo db com a aplicação
    db.init_app(app)
    
    # Uma rota simples para verificar se o aplicativo está funcionando
    @app.route('/')
    def hello():
        return 'Olá, DioBank!'
        
    return app


# Cria uma instância do aplicativo para o CLI do Flask encontrar
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
 