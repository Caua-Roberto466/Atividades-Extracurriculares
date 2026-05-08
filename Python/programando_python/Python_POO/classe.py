class Produto:
    def __init__(self, nome_produto, preco_produto, quantidade_produto):
        self.nome = nome_produto
        self.preco = preco_produto
        self.quantidade = quantidade_produto
    def vender(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade -= quantidade_vendida
            print(f"Foi vendido {quantidade_vendida} {self.nome}(s), agora no estoque tem {self.quantidade}")
        else:
            print(f"Não há {self.nome} suficiente no estoque")
    
    def repor(self, quantidade_reposta):
        self.quantidade += quantidade_reposta
        print(f"{quantidade_reposta} {self.nome} foram repostos, agora tem {self.quantidade} no estoque")


meu_produto = Produto(nome_produto="Lápis", preco_produto=3.99, quantidade_produto=5)
meu_produto.repor(1)
meu_produto.vender(6)