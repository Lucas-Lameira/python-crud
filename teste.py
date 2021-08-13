import sqlite3
import requests
dicionario = {
    "atividade_principal": [
        {
            "text": "Atividades de intermediação e agenciamento de serviços e negócios em geral, exceto imobiliários (Dispensada *)",
            "code": "74.90-1-04"
        }
    ],
    "data_situacao": "02/05/2013",
    "complemento": "ANDAR 3 ANDAR 4 ANDAR 5 ANDAR 6 ANDAR 7",
    "tipo": "MATRIZ",
    "nome": "99 TECNOLOGIA LTDA",
    "uf": "SP",
    "telefone": "(11) 9999-9999/ (11) 8888-8888",
    "atividades_secundarias": [
        {
            "text": "Estacionamento de veículos",
            "code": "52.23-1-00"
        },
        {
            "text": "Desenvolvimento de programas de computador sob encomenda (Dispensada *)",
            "code": "62.01-5-01"
        },
        {
            "text": "Desenvolvimento e licenciamento de programas de computador customizáveis (Dispensada *)",
            "code": "62.02-3-00"
        },
        {
            "text": "Desenvolvimento e licenciamento de programas de computador não-customizáveis",
            "code": "62.03-1-00"
        },
        {
            "text": "Tratamento de dados, provedores de serviços de aplicação e serviços de hospedagem na internet (Dispensada *)",
            "code": "63.11-9-00"
        },
        {
            "text": "Portais, provedores de conteúdo e outros serviços de informação na internet (Dispensada *)",
            "code": "63.19-4-00"
        },
        {
            "text": "Agenciamento de espaços para publicidade, exceto em veículos de comunicação (Dispensada *)",
            "code": "73.12-2-00"
        },
        {
            "text": "Outras atividades de publicidade não especificadas anteriormente",
            "code": "73.19-0-99"
        },
        {
            "text": "Locação de outros meios de transporte não especificados anteriormente, sem condutor",
            "code": "77.19-5-99"
        },
        {
            "text": "Aluguel de equipamentos recreativos e esportivos (Dispensada *)",
            "code": "77.21-7-00"
        },
        {
            "text": "Aluguel de outras máquinas e equipamentos comerciais e industriais não especificados anteriormente, sem operador",
            "code": "77.39-0-99"
        },
        {
            "text": "Atividades de vigilância e segurança privada",
            "code": "80.11-1-01"
        },
        {
            "text": "Atividades de cobranças e informações cadastrais (Dispensada *)",
            "code": "82.91-1-00"
        },
        {
            "text": "Outras atividades de serviços prestados principalmente às empresas não especificadas anteriormente",
            "code": "82.99-7-99"
        },
        {
            "text": "Outraserviços prestados principalmente às empresas não especificadas anteriormente",
            "code": "82.99-814-99"
        }
    ],
    "qsa": [
        {
            "qual": "37-Sócio Pessoa Jurídica Domiciliado no Exterior",
            "pais_origem": "ESTADOS UNIDOS",
            "nome_rep_legal": "GUANGYU QIU",
            "qual_rep_legal": "17-Procurador",
            "nome": "99 TAXIS LLC"
        },
        {
            "qual": "37-Sócio Pessoa Jurídica Domiciliado no Exterior",
            "pais_origem": "CAYMAN, ILHAS",
            "nome_rep_legal": "GUANGYU QIU",
            "qual_rep_legal": "17-Procurador",
            "nome": "99 TAXIS"
        },
        {
            "qual": "05-Administrador",
            "nome": "BRUNO RODRIGUES FURTADO DE MENDONCA"
        }
    ],
    "situacao": "ATIVA",
    "bairro": "CIDADE MONCOES",
    "logradouro": "R SANSAO ALVES DOS SANTOS",
    "numero": "400",
    "cep": "04.571-090",
    "municipio": "SAO PAULO",
    "porte": "DEMAIS",
    "abertura": "02/05/2013",
    "natureza_juridica": "206-2 - Sociedade Empresária Limitada",
    "cnpj": "0008.asd023.552/0001-61",
    "ultima_atualizacao": "2021-07-22T17:43:05.986Z",
    "status": "OK",
    "fantasia": "",
    "email": "",
    "efr": "",
    "motivo_situacao": "",
    "situacao_especial": "",
    "data_situacao_especial": "",
    "capital_social": "751457800.00",
    "extra": {

    },
    "billing": {
        "free": "true",
        "database": "true"
    }
}

def makeRequest(cnpj):
    req = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}").json()

    if req["status"] == "error":
        print(req["status"])

    if req.status_code == 200 and req["status"] == "OK":
        print("works")

# funcionando
def addNewEmpresa():
    try:
        cnpj = '012345asd6'
        nome = 'lucaasds'
        uf = 'pa'
        email = 'lucasasdemail.com'
        data = 'now'

        connection = sqlite3.connect('teste.db')
        cursor = connection.cursor()
        sql = f"INSERT INTO empresa VALUES ('{cnpj}',' {nome}', '{uf}', '{email}', '{data}')"
        print(sql)
        cursor.execute(sql)
        connection.commit()
        print("Nova empresa Cadastrada")
    except sqlite3.Error as error:
        print("Deu erro! ", error)
    finally:
        connection.close()

# funcionando
def listarEmpresas():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        dataRow = cursor.execute("SELECT * FROM empresa").fetchall() # returns a list of tuple
        print("empresas cadastradas:")
        print(dataRow)
    except sqlite3.Error as error:
        print("error: ", error)
    finally:
        connection.close()

def pesquisarUmaEmpresa(cnpj):
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        dataRow = cursor.execute("SELECT * FROM empresa WHERE cnpj = ?", (cnpj,)).fetchall() # return a list[] of tuple ()
        print("empresa encontrada:")
        print(dataRow)
        connection.close()
    except sqlite3.Error as error:
        print("error: ", error)

#funcionando
def inserirEmpresaNoBanco(lista):
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO empresa VALUES (?, ?, ?, ?, ?)", lista)
        connection.commit()
        print("Empresa cadastrada")
        cursor.close()
        connection.close()
    except sqlite3.Error as error:
        print(error)

#funcionando
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

#funcionando
def novaEmpresa():
    colunas = pegarColunasTabela("empresa")
    if colunas:
        print("Tenho colunas")
        print(colunas)
    else:
        print("Nao tenho colunas")

    empresaData = []
    for x in colunas:
        empresaData.append(dicionario.get(x))
    inserirEmpresaNoBanco(empresaData)

#funcionando
def insertIntoServicos():
    a = dicionario["atividade_principal"]
    b = dicionario["atividades_secundarias"]
    c = a + b

    connection = sqlite3.connect("teste.db")
    cursor = connection.cursor()

    for x in c:
        try:
            cursor.execute("INSERT INTO servico VALUES (?, ?)", (x["code"], x["text"]))
            print("Novo serviço adicionado")
        except sqlite3.Error as error:
            print("Proximo, ", error)

    connection.commit()
    connection.close()

#funcionando
def insertIntoListaServicos():
    cnpj = dicionario["cnpj"]

    a = dicionario["atividade_principal"]
    b = dicionario["atividades_secundarias"]
    c = a + b

    connection = sqlite3.connect("teste.db")
    cursor = connection.cursor()
    for x in c:
        try:
            cursor.execute("INSERT INTO lista_servico VALUES (?, ?)", (x["code"], cnpj))
            print("Novo serviço adicionado a lista de serviços")
        except sqlite3.Error as error:
            print("error, ", error)

    connection.commit()
    connection.close()

#funcionando
def listarServicosDeUmaEmpresa(cnpj):
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        d = cursor.execute("""SELECT empresa.nome, servico.descricao
                        FROM empresa INNER JOIN lista_servico
                        ON empresa.cnpj = lista_servico.cnpj
                        JOIN servico
                        ON servico.codigo = lista_servico.codigo
                        WHERE empresa.cnpj = ?""", cnpj).fetchall()
        # d list of tuples [(), ()]
        for x in d:
            print(x)

        connection.close()
    except sqlite3.Error as error:
        print(error)

# funcionando mas falta testar
def cadstrarTelefoneEmpresa():
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()

        if "/" in dicionario["telefone"]:
            telefone = dicionario["telefone"].split("/")
            for x in telefone:
                cursor.execute("INSERT INTO telefone VALUES (?, ?)", (x, dicionario["cnpj"]))
        else:
            cursor.execute("INSERT INTO telefone VALUES (?, ?)", (dicionario["telefone"], dicionario["cnpj"]))
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print(error)

# funcionando
def cadastrarSerivicosPrestados(*tupla):
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO servico_prestado(cnpj_prestador, cnpj_tomador, codigo_servico, data_servico) VALUES (?, ?, ?, ?)", (tupla))
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        print(error)
#cadastrarSerivicosPrestados('0008.asd023.552/0001-61', '0123456', '62.03-1-00', 'now')

# funcionando
def listaSerivicosPrestados(cnpj):
    try:
        connection = sqlite3.connect("teste.db")
        cursor = connection.cursor()
        d = cursor.execute("""SELECT empresa.nome, servico_prestado.codigo_servico, servico.descricao
                        FROM empresa INNER JOIN servico_prestado
                        ON empresa.cnpj = servico_prestado.cnpj_prestador
                        JOIN servico
                        ON servico.codigo = servico_prestado.codigo_servico""").fetchall()
        # d list of tuples [(), ()]
        for x in d:
            print(x)

        connection.close()
    except sqlite3.Error as error:
        print(error)
#listaSerivicosPrestados('0008.asd023.552/0001-61')