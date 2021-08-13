import sqlite3

def createTableEmpresa():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS empresa(
                            cnpj TEXT PRIMARY KEY NOT NULL, 
                            nome TEXT NOT NULL,
                            uf TEXT NOT NULL,
                            email TEXT,
                            data_situacao TEXT NOT NULL)''')
        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)

def createTableServico():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()

        # atividades secundarias e primarias
        cursor.execute('''CREATE TABLE IF NOT EXISTS servico(
                            codigo TEXT NOT NULL PRIMARY KEY,
                            descricao TEXT NOT NULL)''')

        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)

def createTableListaServico():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS lista_servico(
                            codigo TEXT NOT NULL,
                            cnpj TEXT NOT NULL,
                            FOREIGN KEY (cnpj) REFERENCES empresa (cnpj),
                            FOREIGN KEY (codigo) REFERENCES servico (codigo),
                            PRIMARY KEY (codigo, cnpj))''')
        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)

def createTableTelefone():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS telefone(
                            telefone TEXT NOT NULL,
                            cnpj INTEGER NOT NULL,
                            FOREIGN KEY (cnpj) REFERENCES empresa (cnpj)
                            PRIMARY KEY (telefone, cnpj))''')
        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)

def createTableServicoPrestado():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS servico_prestado (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            cnpj_prestador INTEGER NOT NULL,
                            cnpj_tomador INTEGER NOT NULL,
                            codigo_servico TEXT NOT NULL,
                            data_servico TEXT NOT NULL,
                            FOREIGN KEY (cnpj_prestador) REFERENCES empresa (cnpj),
                            FOREIGN KEY (cnpj_tomador) REFERENCES empresa (cnpj))''')
        connection.commit()
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)
