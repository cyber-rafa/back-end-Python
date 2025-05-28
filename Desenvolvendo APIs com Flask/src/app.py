import os

import db  # Importação absoluta em vez de relativa
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import click

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    global db  
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///dio_bank.sqlite',
    )

    if test_config is None:
        
        app.config.from_pyfile('config.py', silent=True)
    else:
        
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)  
    except OSError:
        pass


    app.cli.add_command(init_db_command)
    # Initialize the database
    db.init_app(app)
        
    return app
