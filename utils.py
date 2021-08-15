from os import system, name
from re import sub

def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        # name == posix
        system('clear')


def menu():
    print("============ MENU ==============")
    print("1 - Cadastrar empresa")
    print("2 - Exibir empresas cadastradas")
    print("3 - Buscar uma empresa cadastrada")
    print("4 - Pesquisar os serviços que uma empresa presta")
    print("5 - Cadastrar um novo serviço prestado")
    print("6 - listar serviços prestados por uma empresa")
    print("7 - Atualizar dados de uma empresa cadastrada")
    print("8 - Deletar uma empresa")
    print("9 - Sair")
    print("===============================")


def formata_cnpj(cnpj):
    # remover pontos barra traco
    novo_cpnj = sub(r'[. \- /]', "", cnpj)
    return novo_cpnj
