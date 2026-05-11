class Livro: #Cria a calsse livro
    def __init__(self, titulo, autor): #Cria seu método construtor como parâmetro
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def estado(self): #Cria a função que vê o estado do livro
        if not self.disponivel:
            print("O lvro atualmente se encontra emprestado")
        else:
            print("O livro está disponível")

    def emprestar(self): #Cria a função que vai emprestar o livro se ele estiver disponível
        if not self.disponivel:
            print(f"O livro já foi emprestado")
        else:
            self.disponivel = False
            print(f"O livro {self.titulo} acaba de ser emprestado")
    
    def devolver(self): #Função que vai devolver o livro se ele não estiver disponível
        if self.disponivel:
            print("O livro já foi devolvido")
        else:
            self.disponivel = True
            print("O livro acaba de ser devolvido")

class Biblioteca: #Cria a classe biblioteca
    def __init__(self):
        self.lista = [ #Cria uma lista de Objetos da classe livro
            Livro(titulo="Harry Potter e a Pedra Filosofal", autor="J.K.Rowling"),
            Livro(titulo="Senhor do Anéis", autor="Tokken"),
            Livro(titulo="Flor delicada", autor="Joana Dilja")
        ]

    def adicionar_livro(self): #Função que vai adicionar um objeto na lista, passando os parâmetros com input
        titulo = input("Insira o título: ")
        autor = input("Insira o autor: ")
        for lv in self.lista:
            if titulo in lv.titulo:
                print("Este livro já está registrado")
            else:
                self.lista.append(Livro(titulo, autor))
                print("Livro adicionado com sucesso!\n")
    
    def buscar_por_titulo(self, busca): #Função que encontra um objeto na lista com um for e um if inline na lista
        encontrados = [livro for livro in self.lista if busca.lower() == livro.titulo.lower()]

        if len(encontrados) > 0:
            for livros in encontrados:
                print(f"Título: {livros.titulo} | Autor(a): {livros.autor}")
        else:
            print("Livros não encontrados")
    
    def listar_disponiveis(self): #Vai listar todos os livros em que disponívle é 'True'
        cont = 1
        for livro in self.lista:
            if livro.disponivel:
                print(f"{cont}º Livro: {livro.titulo} | Autor: {livro.autor}")
                cont += 1

minha_biblioteca = Biblioteca()

while True:
    print("\nEscolha o que fazer \
          \n1 - Adicionar livro \
          \n2 - Buscar livro por título \
          \n3 - Listar livros \
          \n4 - pegar livro emprestado\
          \n0 - Sair")
    
    try:
        escolha = int(input("Escola o que fazer: "))
    except ValueError:
        print("Digite um número!")
    else:
        if escolha == 1:
            minha_biblioteca.adicionar_livro()
        elif escolha == 2:
            buscar = input("\nDigite o nome do livro que deseja buscar: ")
            minha_biblioteca.buscar_por_titulo(buscar)
        elif escolha == 3:
            if len(minha_biblioteca.lista) > 0:
                quant = len(minha_biblioteca.lista)
                print("")
                for lv in minha_biblioteca.lista:
                    print(f"Livro: {lv.titulo} | Autor: {lv.autor}")
            else:
                print("Não há livros registrados")
        elif escolha == 4:
            minha_biblioteca.listar_disponiveis()
            try:
                escolha = int(input("Qual livro você que pegar emprestado: "))
            except ValueError:
                print("Digite um número")
            else:
                minha_biblioteca.lista[escolha-1].emprestar()

        elif escolha == 0:
            print("Biblioteca fechando...")
            break