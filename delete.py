import sqlite3
from ler_dados import verificar_empresa_existe

# deletar uma empresa
def deletar_empresa(cnpj):

    if verificar_empresa_existe(cnpj) == 0:
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