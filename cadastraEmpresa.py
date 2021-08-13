import requests
import sqlite3


def pegarColunasTabela(nomeTabela):
    try:
        connection = sqlite3.connect("teste.db")
        sql = F"SELECT * FROM {nomeTabela}"
        cursor = connection.execute(sql)
        colunas = list(map(lambda x: x[0], cursor.description))
        cursor.close()
        connection.close()
        return colunas
    except sqlite3.Error as error:
        print(error)


def makeRequest(cnpj):
    req = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    status_code = req.status_code
    data = req.json()

    if status_code == 504:
        print()
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
    # this should be fine
    connection = sqlite3.connect("teste.db")
    cursor = connection.cursor()

    # item is a dictionary
    for item in servicos:
        try:
            cursor.execute("INSERT INTO servico VALUES (?, ?)", (item["code"], item["text"]))
            print("Novo serviço adicionado")
        except sqlite3.Error as error:
            print("Proximo, ", error)

    connection.commit()
    connection.close()


def cadastrar_lista_servicos_da_empresa(cnpj, servicos):
    connection = sqlite3.connect("teste.db")
    cursor = connection.cursor()

    for item in servicos:
        try:
            cursor.execute("INSERT INTO lista_servico VALUES (?, ?)", (item["code"], cnpj))
            print("Novo serviço adicionado a lista de serviços")
        except sqlite3.Error as error:
            print("error, ", error)

    connection.commit()
    connection.close()


def cadstrar_telefone_empresa(telefone, cnpj):
    try:
        connection = sqlite3.connect("teste.db")
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


def cadastrar_empresa(cnpj):
    data = makeRequest(cnpj)

    if data == 0:
        print("Não foi possivel cadastrar a empresa. Tente mais tarde")
        return 0

    colunas = pegarColunasTabela("empresa")
    empresaData = []
    try:
        for x in colunas:
            empresaData.append(data.get(x))

        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO empresa VALUES (?, ?, ?, ?, ?)", empresaData)
        connection.commit()
        print("Empresa cadastrada")
        connection.close()
    except sqlite3.Error as error:
        print(error)
        return print("Empresa ja cadastrada")

    lista_servicos = data["atividade_principal"] + data["atividades_secundarias"]
    cadastrar_servicos(lista_servicos)
    cadastrar_lista_servicos_da_empresa(data["cnpj"], lista_servicos)
    cadstrar_telefone_empresa(data["telefone"], data["cnpj"])