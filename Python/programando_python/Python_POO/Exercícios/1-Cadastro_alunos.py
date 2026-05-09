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
        soma = 0
        for nota in self.notas:
            soma += nota
        
        quant = len(self.notas)

        media = soma / quant
        return media

aluno1 = Aluno(nome="Jorge", idade=15)
print(f"Notas do aluno {aluno1.nome}\n\n")
try:
    cont = int(input("Quantas notas você quer adicionar? "))
    for i in range(0, cont):
        aluno1.adicionar_nota(valor=(int(input(f"Digite a {i+1}º nota dele: "))))

except ValueError:
    print("Digite apenas número")