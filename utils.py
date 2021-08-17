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
    print("1 - Pesquisar uma empresa na receitaws ")
    print("2 - Cadastrar empresa")
    print("3 - Exibir empresas cadastradas")
    print("4 - Buscar uma empresa cadastrada")
    print("5 - Pesquisar os serviços que uma empresa presta")
    print("6 - Cadastrar um novo serviço prestado")
    print("7 - listar serviços prestados por uma empresa")
    print("8 - Atualizar dados de uma empresa cadastrada")
    print("9 - Deletar uma empresa")
    print("10 - Pesquisar empresa por campo")
    print("11 - Sair")
    print("===============================")


def formata_cnpj(cnpj):
    # remover pontos barra traco
    novo_cpnj = sub(r'[. \- /]', "", cnpj)
    return novo_cpnj

# def formata_telefone(cnpj):