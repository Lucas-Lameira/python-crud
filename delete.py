import sqlite3
from leituraDados import pesquisar_uma_empresa, listar_empresas

# deletar uma empresa
def deletar_empresa(cnpj):
    if listar_empresas() == 0:
        return 0

    # verificar se o cnpj esta no banco
    if pesquisar_uma_empresa(cnpj) == 0:
        return 0

    try:
        connection = sqlite3.connect("banco_dados.db")
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM empresa WHERE cnpj = ?", (cnpj,))
        connection.commit()
        connection.close()
        print("Operção realizada com sucesso!")
    except sqlite3.Error as error:
        print("error", error)