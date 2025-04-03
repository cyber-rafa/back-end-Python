import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()

def criar_tabela(cursor):
    cursor.execute(
        'CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100),'
        'email VARCHAR(150))'
    ) 

def inserir_cliente(cursor, nome, email):
    data = (nome, email)
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
    con.commit()

def atualizar_registro(con, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute(
        'UPDATE clientes SET nome =?, email=? WHERE id=?;', data)
    con.commit()


atualizar_registro(con, cursor, 'rafael willian', 'rafa@gmail.com', 1)



atualizar_registro(con, cursor, 'thais', 'thais@gmail.com', 3)
#nao existe o id 3 entre os registros entao nao vai atualizar nada
