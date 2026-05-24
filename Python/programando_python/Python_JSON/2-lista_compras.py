import json

ARQUIVO = "2-compras.json"

def salvar():
    with open(ARQUIVO, "w", encoding='utf-8') as arq:
        json.dump(compras, arq, indent=4, ensure_ascii=False)

try:
    with open(ARQUIVO, "r", encoding='utf-8') as arq:
        compras = json.load(arq)

except FileNotFoundError:
    compras = []

while True:
    print("")
    print("="*20)
    print("Menu de compras")
    print("1 - Adicionar item à lista")
    print("2 - Listar itens")
    print("0 - Sair")
    print("="*20)

    try:
        escolha = int(input("\nEscolha o que fazer(1, 2 ou 0): "))
        
    except ValueError:
        print("\nDigite um número")
    else:
        if escolha == 1:
            nome = input("\nDigite o nome do produto: ")
            quant = int(input("Digite a quantidade que você vai adicionar: "))
            produto = {
                'nome': nome,
                'quantidade': quant
            }
            compras.append(produto)
            salvar()
            print("\nProduto adicionado")
        elif escolha == 2:
            if not compras:
                print("\nA lista está vazia")
            else:
                print("")
                for item in compras:
                    print(f"Produto: {item['nome']} | Quantidade: {item['quantidade']}")
        elif escolha == 0:
            salvar()
            print("\nPrograma encerrado")
            break