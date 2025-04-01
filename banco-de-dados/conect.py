import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()

#cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')


data = ('thais', 'thais@gmail')
cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', data)
con.commit()
print('Cliente adicionado com sucesso!')
