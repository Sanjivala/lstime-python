import sqlite3
import time

database = 'progressos.db'

conexao = sqlite3.connect(database)
cursor = conexao.cursor()
cursor.execute('select minutos, dataCadastro from progressos')
linhas = cursor.fetchall()
conexao.close()

lista = []

for linha in linhas:
	lista.append(linha)

for items in lista:
	print(items)
	time.sleep(1)