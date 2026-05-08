class Funcionario: #Criando a classe pai
    def __init__(self, nome, salario): #Método construtor
        self.nome = nome
        self.salario = salario
    
    def receber_aumento(self, percentual):
        self.salario = self.salario * (1 + percentual / 100)
        print(f"o funcionário {self.nome} acaba de receber um aumento de {percentual}% e agora recebe {self.salario}")
        return self.salario

class Gerente(Funcionario): #Criando a classe que herda de funcionário
    def __init__(self, nome, salario, departamento): #Método construtor
        super().__init__(nome, salario) #Chama o método construtor da classe pai
        self.departamento = departamento
    
    def apresentar(self): #Declarando função de apresentar
        print(f"Olá, eu sou {self.nome}, gerente do departamento {self.departamento} e recebo R${self.salario}")

#Intânciando
meu_gerente = Gerente(nome="Glauber", salario=8000.00, departamento="Vendas")

meu_gerente.apresentar()