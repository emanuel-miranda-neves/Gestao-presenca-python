registros = []

def exibir_menu():
    print("\n--- GESTAO DE PRESENCA E FALTAS ---")
    print("1. Lancar Ponto do Funcionario")
    print("2. Ver Historico de Lancamentos")
    print("3. Gerar Relatorio Quinzenal (.txt)")
    print("4. Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        nome = input("Nome do funcionario: ")
        data = input("Data (DD/MM): ")
        status = input("Status (P - Presente / F - Falta): ").upper()
        
        registro = {"nome": nome, "data": data, "status": status}
        registros.append(registro)
        print(f"Ponto de {nome} salvo com sucesso!")

    elif opcao == "2":
        print("\n--- HISTORICO DE PONTOS ---")
        if not registros:
            print("Nenhum registro encontrado.")
        else:
            for r in registros:
                print(f"Data: {r['data']} | Funcionario: {r['nome']} | Status: {r['status']}")

    elif opcao == "3":
        print("\n--- GERANDO RELATORIO QUINZENAL ---")
        
        with open("relatorio_quinzenal.txt", "w") as arquivo:
            arquivo.write("--- RELATORIO DE FREQUENCIA QUINZENAL ---\n\n")
            for r in registros:
                arquivo.write(f"Data: {r['data']} - Funcionario: {r['nome']} - Status: {r['status']}\n")
                
        print("Relatorio salvo no arquivo 'relatorio_quinzenal.txt'!")

    elif opcao == "4":
        print("Saindo do programa...")
        break

    else:
        print("Opcao invalida, tente novamente.")