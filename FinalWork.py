#inicializando agenda como dicionario para armazenar os dados
agenda = {}

#Funcoes chamadas pelo programa
def incluir_compromisso(data, hora, descricao)
    if data not in agenda:
        agenda[data]={}
    agenda[data][hora]=descricao

#Inicializacao do programa, selecionando funcoes por numerais

while True:
    print("\nAgenda de Compromissos")
    print("1. Incluir Compromisso")
    print("2. Consultar Compromisso")
    print("3. Alterar Compromisso")
    print("4. Excluir compromisso")
    print("5. Listar Compromissos")
    print("6. Sair da Agenda")
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        data = input("Informe a data (dd/mm/aaaa): ")
        hora = input("Informe a hora (hh:mm): ")
        descricao = input("Informe a descrição: ")

#concatenando os dados em uma funcao
        incluir_compromisso(data, hora, descricao)
    
    if escolha == 5:
        break
    else:
        print("Opção inválida.")