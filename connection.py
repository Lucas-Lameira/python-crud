import sqlite3

connection = sqlite3.connect("teste.db")
cursor = connection.cursor()
data = cursor.execute("""SELECT * FROM empresa""").fetchall()
print(data)

# update
#cursor.execute("UPDATE table SET coluna nomeColuna = valor")
#cursor.execute("UPDATE empresa SET nome = novo_nome")

# delete
#cursor.execute("DELETE FROM empresa WHERE cnpj = 12345678915487")

# save changes
connection.commit()

connection.close()