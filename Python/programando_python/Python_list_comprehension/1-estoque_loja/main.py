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
    print("-"*15)
    print(f"Produto: {produto['nome']}")
    print(f"Preço: {produto['preço']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Quantidade: {produto['quantidade']}")
    print("-"*15)

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
            if len(historico) > 0:
                categoria = input("\nDigite a categoria que deseja buscar: ")
                produtos_cat = [p for p in historico if p['categoria'].lower() == categoria.lower()]

                if len(produtos_cat) > 0:
                    for produto in produtos_cat:
                        exibir_produto(produto)

                else:
                    print(f"\nNão há produtos da categoria {categoria}.")

            else:
                print("\nNão há produtos cadastrados!")
            

        elif escolha == 3:
            por_preco = sorted(historico, key=lambda a: a['preço'])

            if len(por_preco) > 0:
                for produto in por_preco:
                   exibir_produto(produto)
            
            else:
                print("\nNão há produtos cadastrados!")

        else:
            print("Escolha inválida!")