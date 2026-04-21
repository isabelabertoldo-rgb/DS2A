opcao = ""
while opcao != "3":
    print("\n[1] Saudar")
    print("[2] Calcular Dobro")
    print("[3] Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("Olá! Tenha um ótimo dia de aula.")
    elif opcao == "2":
        n = float(input("Digite o número: "))
        print(f"O dobro de {n} é {n*2}")
    elif opcao == "3":
        print("Saindo do sistema...")
    else:
        print("Opção inválida!")