import sqlite3
from ler_dados import listar_empresas, \
    exibir_servicos_empresa, \
    pegar_servico_empresa, \
    verificar_empresa_existe
from validacao import input_cnpj


def cadastrar_serivico_prestado():
    if listar_empresas() == 0:
        return 0

    print("Digite o CNPJ do prestador!")
    cnpj_prestador = input_cnpj()

    if verificar_empresa_existe(cnpj_prestador) == 0:
        return 0

    exibir_servicos_empresa(cnpj_prestador)

    codigo_servico = ''
    while codigo_servico == '' or len(codigo_servico) != 10:
        codigo_servico = input("digite o código do servico: ")

    servico = pegar_servico_empresa(codigo_servico, cnpj_prestador)
    if servico == 0:
        return 0

    print(f"{servico} selecionado!")

    # cnpj tomador
    listar_empresas()

    print("Digite o CNPJ do tomador")
    cnpj_tomador = input_cnpj()

    if cnpj_tomador == cnpj_prestador:
        print("Os CNPJs são iguais")
        return 0

    if verificar_empresa_existe(cnpj_tomador) == 0:
        return 0

    novo_servico = (cnpj_prestador, cnpj_tomador, codigo_servico, "data")

    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO servico_prestado
                            (cnpj_prestador, cnpj_tomador, codigo_servico, data_servico) 
                            VALUES (?, ?, ?, ?)""", novo_servico)
        connection.commit()
        connection.close()

        print("Serviço prestado cadastrado com sucesso!")
        return 1
    except sqlite3.Error as error:
        print(error)
        return 0
