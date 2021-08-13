"""
print(req.status_code)#sempre retorna 200
print(type(req.json())) # returns a dictionarie class?????? guardar isso e testar dps
print(req.json()) # returns a dictionarie string
print(type(req.text)) # returns a string
"""
import requests
import json
import sqlite3

# validar se a key status possui o valor ERROR nele ou se possui o valor OK
#if req.status_code == 200:
#    print("work")
#else:
#    print(f"did not work {req.status_code}")

# converter uma string em um dicionario
#data = json.loads(req.text)
#print(type(data))
#print(data)




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
    "cnpj": "18.033.552/0001-61",
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

"""
# dados a serem armazenados na tabela telefone
print("Dados a serem Armazenados na tabela telefone")
print(dicionario["telefone"])
print(dicionario["cnpj"])

# dados a serem armazenados na tabela serviços
print("Dados a serem Armazenados na tabela servicos")
print(dicionario["atividade_principal"])#list
print(dicionario["atividades_secundarias"])#list
"""
