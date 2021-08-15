from criar_banco import conexao
from utils import menu, limpar_tela
from cadastraEmpresa import cadastrar_empresa

from leituraDados import \
    exibir_servicos_empresa, \
    pesquisar_uma_empresa, \
    listar_empresas, \
    listar_servicos_prestados, \
    isAlgumDado
from validacao import input_cnpj, menu_input
from cadastraNovoServicoPrestado import cadastrar_serivico_prestado

from update import atualizar_empresa
from delete import deletar_empresa

if conexao() == 0:
    raise Exception("DEU RUIM")


isTrue = True
while isTrue:

    # print menu list
    menu()
    answer = menu_input(1, 9)

    # sodades switch case
    if answer == 1:
        cadastrar_empresa()

    elif answer == 2:
        limpar_tela()
        listar_empresas()

    elif answer == 3:
        isOk = isAlgumDado()
        if not isOk:
            print("....")
        else:
            cnpj = input_cnpj()
            limpar_tela()
            pesquisar_uma_empresa(cnpj)

    elif answer == 4:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()

            limpar_tela()
            exibir_servicos_empresa(cnpj)

    elif answer == 5:
        cadastrar_serivico_prestado()

    elif answer == 6:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            listar_servicos_prestados(cnpj)

    elif answer == 7:

        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            atualizar_empresa(cnpj)

    elif answer == 8:
        if listar_empresas() == 0:
            print("....")
        else:
            cnpj = input_cnpj()
            deletar_empresa(cnpj)

    elif answer == 9:
        print("saindo.....")
        break

    # check if the user wants to continue
    answer = input("Deseja continuar s/n: ")
    answer = answer.lower()
    while answer != 's' and answer != 'n':
        print("Digite 's' pra sim ou 'n' para não")
        answer = input("Deseja continuar s/n: ")

    if answer == 'n':
        isTrue = False
    limpar_tela()
