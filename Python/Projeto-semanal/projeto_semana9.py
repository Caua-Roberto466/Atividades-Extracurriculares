#Cadastro de usuários
ususarios_cadstrados = []

while True:
    print("\nO que deseja fazer?\
        \n1 - Cadastrar usuário\
        \n2 - Ver usuários cadastrados\
        \n0 - Sair do programa")
    escolha = int(input("Escolha entre 1, 2 ou 0 "))

    if escolha == 1:
        usuario = input("\nInsira o usuário que deseja cadastrar: ")
        if usuario in ususarios_cadstrados:
            print("Usuário já cadastrado")
        else:
            ususarios_cadstrados.append(usuario)
            print(f"\nUsuário {usuario} cadastrado com sucesso")
    elif escolha == 2:
        if len(ususarios_cadstrados) != 0:
            for i in range(len(ususarios_cadstrados)):
                print(f"Usuário: {ususarios_cadstrados[i]}")
        else:
            print("\nNão há usuários cadastrados")
    elif escolha == 0:
        print("Programa encerrado")
        break
    else:
        print("Opção inválida")