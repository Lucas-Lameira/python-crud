import sqlite3
from os import path


def conexao():
    if path.isfile('banco_dados.db'):
        print("Iniciando software....")
        return 1
    else:
        try:
            connection = sqlite3.connect("banco_dados.db")
            connection.execute("PRAGMA foreign_keys = ON")
            cursor = connection.cursor()

            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS empresa(
                    cnpj TEXT PRIMARY KEY NOT NULL, 
                    nome TEXT NOT NULL,
                    uf TEXT NOT NULL,
                    email TEXT,
                    data_situacao TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS servico(
                    codigo TEXT NOT NULL PRIMARY KEY,
                    descricao TEXT NOT NULL
                );

                CREATE TABLE IF NOT EXISTS lista_servico(
                    codigo TEXT NOT NULL,
                    cnpj TEXT NOT NULL,
                    FOREIGN KEY (cnpj) 
                    REFERENCES empresa (cnpj) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                    FOREIGN KEY (codigo) 
                    REFERENCES servico (codigo) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                    PRIMARY KEY (codigo, cnpj)
                );

                CREATE TABLE IF NOT EXISTS telefone(
                    telefone TEXT NOT NULL,
                    cnpj INTEGER NOT NULL,
                    FOREIGN KEY (cnpj) 
                    REFERENCES empresa (cnpj) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                    PRIMARY KEY (telefone, cnpj)
                );

                CREATE TABLE IF NOT EXISTS servico_prestado (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    cnpj_prestador INTEGER NOT NULL,
                    cnpj_tomador INTEGER NOT NULL,
                    codigo_servico TEXT NOT NULL,
                    data_servico TEXT NOT NULL,
                    FOREIGN KEY (cnpj_prestador) 
                    REFERENCES empresa (cnpj) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE,
                    FOREIGN KEY (cnpj_tomador) 
                    REFERENCES empresa (cnpj) 
                    ON DELETE CASCADE 
                    ON UPDATE CASCADE
                );
            """)

            connection.commit()

        except sqlite3.Error as error:
            print("Não foi possivel criar o banco de dados...\n", error)
            return 0
    return 1
