import sqlite3
from validacao import input_cnpj


# ok
def listar_empresas():
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()

        # returns a list of tuple. each tuple is a row in the table
        empresas = cursor.execute("SELECT * FROM empresa").fetchall()

        connection.close()

        # remember to test if there is no data
        if len(empresas) == 0:
            print("Você não cadastrou nenhuma empresa ainda!")
            return 0

        print(f"{'=' * 40} Empresas cadastradas {'=' * 40}")

        print(f"CNPJ{' ' * 16}|nome{' ' * 24}|UF  |Email{' ' * 15}|Data de abertura")
        for item in empresas:
            for x in item:
                print(x, end=" ")
            print('')
        print(f"{'=' * 80}")
    except sqlite3.Error as error:
        print("Ops!... Algo deu errado...\n", error)
        return 0


def verificar_empresa_existe(cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        dataRow = cursor.execute("SELECT * FROM empresa WHERE cnpj = ?", (cnpj,)).fetchall()  # return a list of tuple
        connection.close()

        if len(dataRow) == 0:
            print(f"Empresa com CNPJ:{cnpj} não foi encontrada!")
            return 0
        else:
            return 1
    except sqlite3.Error as error:
        print("error: ", error)
        return 0


# ok
def pesquisar_uma_empresa(cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()

        # return a list of tuple
        dataRow = cursor.execute("SELECT * FROM empresa WHERE cnpj = ?", (cnpj,)).fetchall()

        if len(dataRow) == 0:
            print(f"Empresa com CNPJ:{cnpj} não foi encontrada!")
            return 0  # new line
        else:
            row = dataRow[0]
            print(f"{'=' * 30} Dados {'=' * 30}")
            print(f"CNPJ{' ' * 16} |nome{' ' * len(row[1])} |UF   |Email{' ' * len(row[3])} |Data de abertura")

            for item in row:
                print(item, end=' ')
            print('')
        connection.close()
    except sqlite3.Error as error:
        print("error: ", error)


# ok
def exibir_servicos_empresa(cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        # servicos é um list de tuples [(), ()]
        servicos = cursor.execute("""SELECT empresa.nome, servico.codigo, servico.descricao
                        FROM empresa INNER JOIN lista_servico
                        ON empresa.cnpj = lista_servico.cnpj
                        JOIN servico
                        ON servico.codigo = lista_servico.codigo
                        WHERE empresa.cnpj = ?""", (cnpj,)).fetchall()


        connection.close()

        if len(servicos) == 0:
            return print("Nenhum serviço encontrado")

        nome_empresa = servicos[0][0]
        print(f"{'=' * 40} {nome_empresa} {'=' * 40}")
        print(f"Codigo {' ' * 5} Serviços")

        for items in servicos:
            for item in range(len(items) - 1):
                print(items[item + 1], end='   ')
            print('')

        print(f"{'=' * 82}{'=' * len(nome_empresa)}")
    except sqlite3.Error as error:
        print(error)


# funcionando
def listar_servicos_prestados(cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        data = cursor.execute("""SELECT empresa.nome, servico_prestado.codigo_servico, servico.descricao
                        FROM empresa INNER JOIN servico_prestado
                        ON empresa.cnpj = servico_prestado.cnpj_prestador
                        JOIN servico
                        ON servico.codigo = servico_prestado.codigo_servico
                        WHERE empresa.cnpj = ?""", (cnpj,)).fetchall()

        connection.close()

        if len(data) == 0:
            print(f"Lista de serviços prestados vazia, não há serviços prestados por esta empresa!")
            return 0
        else:
            print("========Servicos Prestados!========")
            print("Empresa x")

        # d list of tuples [(), ()]
        for items in data:
            for item in items:
                print(item, end=' ')
            print('')

    except sqlite3.Error as error:
        print(error)


def pegar_servico_empresa(codigo, cnpj):
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        data = cursor.execute("""SELECT empresa.nome, servico.descricao
                        FROM empresa INNER JOIN lista_servico
                        ON empresa.cnpj = lista_servico.cnpj
                        JOIN servico
                        ON servico.codigo = lista_servico.codigo
                        WHERE empresa.cnpj = ? AND servico.codigo = ?""", (cnpj, codigo)).fetchall()

        connection.close()

        if len(data) == 0:
            print(f"Essa empresa não disponibiliza este servico!")
            return 0
        else:
            return data[0][1]  # returns a tuple
    except sqlite3.Error as error:
        print(error)
        return 0


def isAlgumDado():
    try:
        connection = sqlite3.connect("banco_dados.db")
        cursor = connection.cursor()
        data = cursor.execute("SELECT * FROM empresa").fetchall()
        connection.close()

        if len(data) == 0:
            print("Nenhuma empresa cadastrada")
            return False
        else:
            return True
    except sqlite3.Error as error:
        print(error)
        return False
