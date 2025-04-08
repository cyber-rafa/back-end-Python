import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent


con = sqlite3.connect(ROOT_PATH / 'banco.sqlite')
cursor = con.cursor()
cursor.row_factory = sqlite3.Row

id_cliente = input('Digite o id do cliente: ')

cursor.execute(f'SELECT * FROM clientes WHERE id={id_cliente}')
cliente = cursor.fetchall()

for cliente in cliente:
    print(dict(cliente))