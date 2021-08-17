import sqlite3
from cadastra_empresa import pegar_colunas_tabela
from ler_dados import pesquisar_uma_empresa, listar_empresas
from validacao import menu_input, input_cnpj
from utils import limpar_tela


def atualizar_empresa(cnpj):
    if listar_empresas() == 0:
        return 0

    if pesquisar_uma_empresa(cnpj) == 0:
        print("Não foi possível encontrar os dados da empresa!")
        return 0

    colunas = pegar_colunas_tabela("empresa")
    tamanho = len(colunas)

    limpar_tela()

    print(f"{'=' * 10} Escolha um dado para ser atualizado {'=' * 10}")
    for i in range(tamanho):
        print(f"{i+1} - {colunas[i]}")

    print("Digite um número correspondente as opções acima!")
    resposta = menu_input(1, tamanho)

    novo_valor = ''
    if resposta == 1:
        novo_valor = input_cnpj()
    else:
        while novo_valor == '' or novo_valor == cnpj:
            novo_valor = input("Qual o novo valor a ser atualizado: ")

    campo = colunas[resposta - 1]

    # vulnerable to sql injection and only works for string values
    sql = f"UPDATE empresa SET {campo} = '{novo_valor}' WHERE cnpj = '{cnpj}'"

    try:
        connection = sqlite3.connect("banco_dados.db")
        connection.execute("PRAGMA foreign_keys = ON")
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()
        print("Operação feita com sucesso")
    except sqlite3.Error as error:
        print("error", error)