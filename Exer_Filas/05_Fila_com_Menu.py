fila = []

while True:
    print("\n---MENU---")
    print("1 - Adicionar pessoa")
    print("2 - Atender pessoa")
    print("3 - Mostrar fila")
    print("4 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        nome = input("Nome da pessoa: ")
        fila.append(nome)
        print("Pessoa adicionada a fila.")
    elif opcao == 2:
        if len(fila) > 0:
            pessoa = fila.pop(0)
            print("Pessoa atendida:", pessoa)
        else:
            print("Fila vazia")
    elif opcao == 3:
        print("Fila:", fila)
    elif opcao == 4:
        print("Programa encerrado!")
        break
    else:
        print("ERRO! Digite uma opcao valida!")
    