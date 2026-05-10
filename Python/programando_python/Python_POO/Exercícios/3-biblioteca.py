class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True

    def estado(self):
        if not self.__disponivel:
            print("O lvro atualmente se encontra emprestado")
        else:
            print("O livro está disponível")

    def emprestar(self):
        if not self.__disponivel:
            print("O livro já foi emprestado")
        else:
            self.__disponivel = False
            print("O livro acaba de ser emprestado")
    
    def devolver(self):
        if self.__disponivel:
            print("O livro já foi devolvido")
        else:
            self.__disponivel = True
            print("O livro acaba de ser devolvido")

class Biblioteca:
    def __init__(self):
        self.lista = [
            Livro(titulo="Harry Potter e a Pedra Filosofal", autor="J.K.Rowling"),
            Livro(titulo="Senhor do Anéis", autor="Tokken"),
            Livro(titulo="Flor delicada", autor="Joana Dilja")
        ]

    def adicionar_livro(self):
        self.lista.append(Livro(titulo=(input("Qual o título ")), autor=(input("Qual o autor? "))))
    
    def buscar_por_titulo(self):
        busca = input("Digite o título do livro: ")
        encontrados = [livro for livro in self.lista if busca.lower() in livro.__titulo.lower()]

        if len(encontrados) > 0:
            for livros in encontrados:
                print(f"Título: {livros.__titulo} | Autor(a): {livros.__autor}")
        else:
            print("Livros não encontrados")

while True:
    print("Escolha o que fazer \
          \n1 - Adicionar livro \
          \n2 - Buscar livro por título \
          \n3 - ")