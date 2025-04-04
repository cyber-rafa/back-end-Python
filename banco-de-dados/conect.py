import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

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

def deletar_registro(con, cursor, id):
    data = (id,)
    cursor.execute(
        'DELETE FROM clientes WHERE id=?;', data)
    con.commit()

def inserir_muitos(con, cursor, dados):
    cursor.executemany('INSERT INTO clientes (nome, email) VALUES (?, ?)', dados)
    con.commit()

#dados = [
    #('rafa', 'rafa@gmail'),
    #('thais', 'thais@gmail'),
    #('pedro', 'pedro@gmail'),
#]


def recuperar_clentes(cursor, id):
    cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
    return cursor.fetchone()

def list_clentes(cursor):
    return cursor.execute('SELECT * FROM clientes ORDER BY nome')

clientes = list_clentes(cursor)
for cliente in clientes:
    print(dict(cliente))
    print(cliente['id'], cliente['nome'], cliente['email'])
