from historico import carregar, salvar

def menu():
    print("")
    print("-="*25)
    print("O que deseja fazer?")
    print("1 - Cadastrar produto")
    print("2 - Buscar produto por categoria")
    print("3 - Ordenar por preço")
    print("4 - Calcular valor do estoque")
    print("5 - Relatório final")
    print("0 - Sair")
    print("-="*25)

def exibir_produto(produto):
    print("")
    print("-"*25)
    print(f"Produto: {produto['nome']}")
    print(f"Preço: R${produto['preço']:.2f}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-"*25)

historico = carregar()

while True:
    menu()
    
    try:
        escolha = int(input("O que fazer? "))

    except ValueError:
        print("Digite um número")

    else:

        if escolha == 1:
            nome = input("\nDigite o nome do produto: ")
            preco = float(input("Digite preço do produto: "))
            categoria = input("Digite a categoria do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            
            produto = {
                'nome': nome,
                'preço': preco,
                'categoria': categoria,
                'quantidade': quantidade
            }

            historico.append(produto)
            salvar(historico)


        elif escolha == 2:
            if not historico:
                print("\nNão há produtos cadastrados!")

            else:
                categoria = input("\nDigite a categoria que deseja buscar: ")
                produtos_cat = [p for p in historico if p['categoria'].lower() == categoria.lower()]

                if not produtos_cat:
                    print(f"\nNão há produtos da categoria {categoria}.")
                    

                else:
                    for produto in produtos_cat:
                        exibir_produto(produto)
            

        elif escolha == 3:
            por_preco = sorted(historico, key=lambda a: a['preço'])

            if not por_preco:
                print("\nNão há produtos cadastrados!")
            
            else:
                for produto in por_preco:
                   exibir_produto(produto)
                
        
        elif escolha == 4:
            if not historico:
                print("\nNão há produtos cadastrados!")

            else:
                for produto in historico:
                    print("")
                    exibir_produto(produto)
                    print(f"Total: R${produto['preço']*produto['quantidade']:.2f}")

                total_prod = sum(p['preço']*p['quantidade'] for p in historico)
                print("")
                print("-="*20)
                print(f"Total dos produtos: {total_prod:.2f}")
                print("-="*20)

        elif escolha == 5:
            print("")
            for i, produto in enumerate(historico, start=1):
                print(f"{i} - {produto['nome']}: R${produto['preço']:.2f}")

        elif escolha == 0:
            print(f"\nPrograma encerrado.")
            break

        else:
            print("\nEscolha inválida!")