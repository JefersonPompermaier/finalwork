# inicializando agenda como dicionario para armazenar os dados
agenda = {}

# Funcoes chamadas pelo programa

# funcao para inserir compromisso na data informada


def inserir_compromisso(data, hora, descricao):
    if data not in agenda:
        agenda[data] = {}
    agenda[data][hora] = descricao

# funcao para verificar se ja existem compromissos salvos


def incluir_novo_compromisso(data, hora, descricao):

    if data in agenda and hora in agenda[data]:
        print("Ja existem compromissos neste horário. Tente verificar e alterar o compromisso.")
        return
    else:
        inserir_compromisso(data, hora, descricao)

# funcao para encontrar compromissos por data e hora ou somente por data


def consult_compromisso(data, hora=None):
    if data not in agenda:
        print("Nenhum compromisso encontrado nesta data.")
        return
    if hora:
        if hora in agenda[data]:
            print(agenda[data][hora])
        else:
            print("Nenhum compromisso encontrado nesta hora.")

# se a leitura de hora for igual a 0 o programa retorna todos os compromissos da data especificada
    if hora is not None and len(hora) == 0:
        print(agenda[data])

# funcao para alterar compromissos


def alt_compromisso(data, hora, descricao):
    if data not in agenda:
        print("Nenhum compromisso nesta data e hora, será incluído um novo compromisso.\n")
        inserir_compromisso(data, hora, descricao)
    else:
        inserir_compromisso(data, hora, descricao)


# Inicializacao do programa, selecionando funcoes por numerais

while True:
    print("\nAgenda de Compromissos")
    print("1. Incluir Compromisso")
    print("2. Consultar Compromisso")
    print("3. Alterar Compromisso")
    print("4. Excluir compromisso")
    print("5. Listar Compromissos")
    print("6. Sair da Agenda")

# inseri a variavel como string para caso o usuario digite de forma incorreta o programa de erro
    escolha = str(input("Escolha uma opção: "))

    if escolha == '1':
        data = input("Informe a data (dd/mm/aaaa): ")
        hora = input("Informe a hora (hh:mm): ")
        descricao = input("Informe a descrição: ")
# concatenando os dados em uma funcao
        incluir_novo_compromisso(data, hora, descricao)
    elif escolha == '2':
        data = input("Informa a data que deseja consultar (dd/mm/aaaa): ")
        hora = input(
            "Informe a hora (hh:mm) que deseja consultar (não inclua nada para ver a agenda do dia):")
        consult_compromisso(data, hora)

    elif escolha == '3':
        data = input(
            "Informe a data do compromisso que deseja alterar (dd/mm/aaaa):")
        hora = input(
            "Informe a hora do compromisso que deseja alterar (hh:mm): ")
        descricao = input("Informe a descrição do compromisso: ")
        alt_compromisso(data, hora, descricao)
    elif escolha == '5':
        print(agenda)

    elif escolha == '6':
        break

    else:
        print("\nOpção inválida ou incorreta.")
