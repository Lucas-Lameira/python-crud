from cadastra_empresa import fazer_requisicao, cadastrar_empresa
from validacao import input_cnpj

def exibir_dados_api():
    cnpj = input_cnpj()
    dados = fazer_requisicao(cnpj)

    if dados == 0:
        return 0

    print("Atividade primária: ")
    for item in dados["atividade_principal"]:
        print(f" - {item['text']}")

    # atividade secundaria
    print("Atividades secundarias: ")
    for item in dados["atividades_secundarias"]:
        print(f" - {item['text']}")

    #nome
    print(f"Nome: {dados['nome']}")

    #uf
    print(f"UF: :{dados['uf']}")

    # telefone
    print(f"Telefone: {dados['telefone']}")

    # email
    if dados["email"] == '':
        print("Nenhum email cadastrado")
    else:
        print(f"Email: {dados['email']}")

    # data abertura
    print(f"Data abertura: {dados['data_situacao']}")

    # check if the user wants to continue
    resposta = input("Gostaria de cadastrar esta empresa: s/n: ")
    resposta = resposta.lower()
    while resposta != 's' and resposta != 'n':
        print("Digite 's' pra sim ou 'n' para não")
        resposta = input("Gostaria de cadastrar esta empresa: s/n: ")

    if resposta == 's':
        cadastrar_empresa(dados)


#exibir_dados_api()