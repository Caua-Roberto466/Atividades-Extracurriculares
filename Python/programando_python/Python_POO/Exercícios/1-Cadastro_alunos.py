class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []
    
    def adicionar_nota(self, valor):
            if valor < 0 or valor > 10:
                raise ValueError("Coloque uma nota entre 0 e 10.")
            else:
                self.notas.append(valor)
    
    def media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)
    
alunos = [
    Aluno(nome="Jorge",idade=15),
    Aluno(nome="Caio", idade=16),
    Aluno(nome="Miguel", idade=19)
]

for aluno in alunos:
    print(f"Notas do aluno {aluno.nome}")
    try:
        cont = int(input("Quantas notas você quer adicionar? "))
        for i in range(0, cont):
            aluno.adicionar_nota(int(input(f"Insira a {i+1}º nota do {aluno.nome} ")))
    except ValueError as e:
        print(e)
    else:
        print(f"A média do {aluno.nome} é: {aluno.media()}")