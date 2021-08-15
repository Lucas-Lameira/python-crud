import requests
import sqlite3
from validacao import input_cnpj
from utils import formata_cnpj


def pegar_colunas_tabela(nomeTabela):
    try:
        connection = sqlite3.connect("banco_dados.db")
        sql = F"SELECT * FROM {nomeTabela}"
        cursor = connection.execute(sql)
        colunas = list(map(lambda x: x[0], cursor.description))
        cursor.close()
        connection.close()
        return colunas
    except sqlite3.Error as error:
        print(error)


def fazer_requisicao(cnpj):
    req = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    status_code = req.status_code
    data = req.json()

    if status_code == 504:
        print(f"HTTP {status_code} Time out error!")
        return 0

    if data["status"] == "ERROR":
        print(data["status"])
        print(data["message"])
        return 0

    if status_code == 200 and data["status"] == "OK":
        print("Requisição feita!")
        return data

    if status_code != 200:
        print("somenthing went wrong, status:", status_code)
        print("Error: ", data)
        return 0


def cadastrar_servicos(servicos):
    connection = sqlite3.connect("banco_dados.db")
    cursor = connection.cursor()

    # item is a dictionary
    for item in servicos:
        try:
            cursor.execute("INSERT INTO servico VALUES (?, ?)", (item["code"], item["text"]))
        except sqlite3.Error as error:
            print("Proximo, ", error)

    connection.commit()
    connection.close()


def cadastrar_lista_servicos_da_empresa(cnpj, servicos):
    connection = sqlite3.connect("banco_dados.db")
    cursor = connection.cursor()

    for item in servicos:
        try:
            cursor.execute("INSERT INTO lista_servico VALUES (?, ?)", (item["code"], cnpj))
        except sqlite3.Error as error:
            print("error, ", error)

    connection.commit()
    connection.close()


def cadstrar_telefone_empresa(telefone, cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()

        if "/" in telefone:
            telefones = telefone.split("/")
            for item in telefones:
                cursor.execute("INSERT INTO telefone VALUES (?, ?)", (item, cnpj))
        else:
            cursor.execute("INSERT INTO telefone VALUES (?, ?)", (telefone, cnpj))
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print(error)


def cadastrar_empresa():
    cnpj = input_cnpj()
    data = fazer_requisicao(cnpj)

    if data == 0:
        print("Não foi possivel cadastrar a empresa. Tente mais tarde!")
        return 0

    # as colunas da tabela tem os mesmos nomes das chaves do dicionario que veio da requisicao
    colunas = pegar_colunas_tabela("empresa")
    index_cnpj = colunas.index("cnpj")

    # lista vazia para armazenar os dados pertinentes da requisição
    dados_empresa = []

    try:
        for x in colunas:
            dados_empresa.append(data.get(x))

        dados_empresa[index_cnpj] = formata_cnpj(dados_empresa[index_cnpj])

        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO empresa VALUES (?, ?, ?, ?, ?)", dados_empresa)
        connection.commit()
        print("Empresa cadastrada")
        connection.close()
    except sqlite3.Error as error:
        print(error)
        return print("Empresa ja cadastrada")

    lista_servicos = data["atividade_principal"] + data["atividades_secundarias"]
    cadastrar_servicos(lista_servicos)
    cadastrar_lista_servicos_da_empresa(dados_empresa[index_cnpj], lista_servicos)
    cadstrar_telefone_empresa(data["telefone"], dados_empresa[index_cnpj])