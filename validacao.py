

# vlaidar cnpj
def input_cnpj():
    cnpj = ''
    so_numeros = False

    while not so_numeros or len(cnpj) != 14:
        cnpj = input("Digite os 14 números de um CNPJ válido: ")
        so_numeros = cnpj.isdigit()

    return cnpj


def menu_input(min, max):
    so_numeros = False

    while not so_numeros:
        answer = input("Selecione uma opção:  ")

        so_numeros = answer.isdigit()

        if so_numeros:
            answer = int(answer)

        if so_numeros and min <= answer <= max:
            return answer
        else:
            print(f"Digite um número de {min} a {max}!")
            so_numeros = False
