from cadastraEmpresa import cadastrar_empresa
import sys #pausar o console
import requests
import platform
import os

""" limpar a tela XD, se sobrar tempo
sistema_operacional = str(platform.system()) # Windows or Linux  mac xamais
if sistema_operacional.upper() == "WINDOWS":
    os.system('cls')
elif sistema_operacional.upper() == "LINUX":
    os.system('clear')
"""

def menu():
    print("============ MENU ==============")
    print("1 - Cadastrar empresa")
    print("2 - Exibir empresas cadastradas")
    print("3 - Buscar uma empresa cadastrada")
    print("4 - Atualizar dados de uma empresa cadastrada")
    print("5 - Deletar uma empresa")
    print("6 - Sair")
    print("===============================")

isTrue = True
while isTrue:
    answer = None

    # print menu list
    menu()

    # validate user input
    try:
         answer = int(input("Selecione uma opção: "))
         if answer < 1 or answer > 6:
             raise Exception("Digite um número válido correspondente as opções do menu")
    except:
        print("DIgite um número válido correspondente as opções do menu")
        continue

    # operate based on user input
    if answer == 1:
        cnpj = None

        # validate cnpj
        try:
            cnpj = input("Digite o cnpj da empresa: ")

            if len(cnpj) != 14:
                raise Exception("Um CNPJ deve conter 14 digitos numericos")

            # check if there is any non numeric values
            for x in cnpj:
                int()
        except:
            print("Um CNPJ deve conter 14 digitos numericos")
            break

        cadastrar_empresa(cnpj)

    elif answer == 2:
        print("hello")

    # check if the user wants to continue
    answer = input("Deseja continuar s/n: ")
    answer = answer.lower()
    while answer != 's' and answer != 'n':
        print("Digite 's' pra sim ou 'n' para não")
        answer = input("Deseja continuar s/n: ")

    if answer == 'n':
        isTrue = False