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
            pass