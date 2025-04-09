import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

try:
    cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', ('erro', 'erro@gmail'))
    #con.commit() # Descomente o commit  para ver o erro
    cursor.execute('INSERT INTO clientes (id, nome, email) VALUES (?, ?)', ( 2, 'carlos', 'carlos@gmail'))
    con.commit()
except Exception as exc:
    print('Erro a inserir dados voce estar passando um argumento em um id ja existente', exc)
    con.rollback()