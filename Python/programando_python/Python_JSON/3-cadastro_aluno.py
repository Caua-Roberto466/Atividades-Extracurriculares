import json

ARQUIVO = "3-alunos.json"

class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.notas = []
    
    def adicionar_nota(self, valor):
        if valor < 0 or valor > 10:
            raise ValueError("\nDigite um valor entre 0 e 10")
        else:
            self.notas.append(valor)
            print("\nNotas adicionada com sucesso!")

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

def carregar():
    try:
        with open(ARQUIVO, "r", encoding='utf-8') as arq:
            return json.load(arq)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    
def salvar(lista):
    with open(ARQUIVO, "w", encoding='utf-8') as arq:
        json.dump(lista, arq, indent=4, ensure_ascii=False)

def aluno_dic(aluno):
    return {
        "nome": aluno.nome,
        "idade": aluno.idade,
        "notas": aluno.notas
    }

alunos = carregar()

while True:
    print("")
    print("="*20)
    print("Menu de compras")
    print("1 - Cadastrar aluno")
    print("2 - Adicionar nota")
    print("3 - Listar alunos")
    print("4 - Buscar por nome")
    print("0 - Sair")
    print("="*20)

    try:
        escolha = int(input("Escolha entre 1, 2, 3, 4 ou 0: "))
    except ValueError:
        print("\nDigite um número inteiro")
    else:
        if escolha == 1:
            nome = input("\nDigite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            aluno = Aluno(nome, idade)
            aluno_n = aluno_dic(aluno)
            alunos.append(aluno_n)
            salvar(alunos)
        elif escolha == 2:
            nome = input("\nDigite o nome do aluno: ")
            encontrado = next((a for a in alunos if a['nome'].lower() == nome.lower()), None)
            if not encontrado:
                print("\nAluno não encontrado")
            else:
                try:
                    nota = float(input("\nDigite a nota do aluno: "))
                    aluno_obj = Aluno(encontrado['nome'], encontrado['idade'])
                    aluno_obj.notas = encontrado['notas']
                    aluno_obj.adicionar_nota(nota)
                    encontrado['notas'] = aluno_obj.notas
                    salvar(alunos)
                except ValueError as e:
                    print(f"Erro: {e}")
        elif escolha == 3:
            print("")
            for aln in alunos:
                print(f"Nome: {aln['nome']} | Idade: {aln['idade']}")
        elif escolha == 4:
            nome = input("\nDigite o nome do aluno: ")
            encontrar = next((a for a in alunos if nome.lower() in a['nome'].lower()), None)
            if not encontrar:
                print("\nAluno não encontrado")
            else:
                aluno_obj = Aluno(encontrar['nome'], encontrar['idade'])
                aluno_obj.notas = encontrar['notas']
                media = aluno_obj.calcular_media()

                print(f"\nNome: {encontrar['nome']} | Idade: {encontrar['idade']}")
                print(f"Notas: {encontrar['notas']} | Média: {media}")
        elif escolha == 0:
            salvar(alunos)
            print("Programa encerrado")
            break
        else:
            print("Digite um número válido")